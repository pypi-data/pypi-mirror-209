"""
"""

# flake8: noqa: E241    # (ignore "multiple spaces after ',' ")

import numpy as np
import scipy as sp
import scipy.stats

import kalepy as kale
import kalepy.utils
from kalepy import utils


class Test_IsIntegral:

    def test_int(self):
        goods = [1, -5, int('3'), np.int32(72), np.int64(-123), np.uint(8)]
        bads = ['3', 1.2, float(1)]

        for gg in goods:
            assert utils.isinteger(gg), f"`{gg}` returned False, should be True!"

        for bb in bads:
            assert not utils.isinteger(bb), f"`{bb}` returned False, should be True!"

    def test_array(self):
        goods = [
            [12345],
            [1, 2, 3],
            (3, 4, 5),
            np.arange(10),
            np.arange(10).astype(np.int32),
            np.arange(10).astype(int),
        ]
        bads = [
            [],
            [1.0, 2.2],
            ['1', '2'],
            '123',
            np.arange(10).astype('float'),
        ]

        for gg in goods:
            assert utils.isinteger(gg), f"`{gg}` returned False, should be True!"

        for bb in bads:
            assert not utils.isinteger(bb), f"`{bb}` returned True, should be False!"


class Test_Bound_Indices:

    def test_1d(self):
        aa = np.random.uniform(*[-100, 100], 1000)
        bounds = [-23, 43]
        print(aa)
        print(bounds)

        for out in [False, True]:
            idx = utils.bound_indices(aa, bounds, outside=out)
            test_yes = aa[idx]
            test_not = aa[~idx]
            print("\n", out, idx)

            for val, test in zip([out, not out], [test_yes, test_not]):
                if len(test) == 0:
                    continue

                outside = (test < bounds[0]) | (bounds[1] < test)
                inside = (bounds[0] < test) & (test < bounds[1])

                print("outside = {}, out = {}, val = {}".format(np.all(outside), out, val))
                assert np.all(outside == val)

                print("inside  = {}, out = {}, val = {}".format(np.all(inside), out, val))
                assert np.all(inside == (not val))

        return


class Test_Centroids:

    def _manual_single_1d(self, xx, yy):
        """Analytically calculate the centroid for a single bin in 1D"""
        print(f"xx={xx}, yy={yy}")
        ilo = np.argmin(yy)
        ihi = np.argmax(yy)
        ylo, yhi = yy[ilo], yy[ihi]
        xlo, xhi = xx[ilo], xx[ihi]
        wid = np.fabs(np.diff(xx))

        # calculate center of mass of square portion of trapezoid, and mass of square
        x1 = np.mean(xx)
        m1 = wid * ylo

        # calculate center of mass of triangle portion of trapezoid, and mass of triangle
        x2 = xlo
        x2 += (2.0/3.0) * (xhi - xlo)
        m2 = 0.5 * wid * (yhi - ylo)

        # find overall COM as weighted avereage of component COMs
        com = ((x1 * m1) + (x2 * m2)) / (m1 + m2)
        return com

    def _manual_single_2d(self, edges, data):
        """Analytically calculate the centroid for a single bin in 2D"""
        coms = np.zeros((2, 1, 1))
        for ii in range(2):
            xx = edges[ii]
            # marginalize (sum) over the *other* axis, and calculate in 1D for each dim
            jj = (ii + 1) % 2
            yy = np.sum(data, axis=jj)
            coms[ii] = self._manual_single_1d(xx, yy)

        return coms

    def _numeric(self, edges, data, num=1e5):
        """Numerically calculate the centroid by sampling `num` points over the grid

        This works for any number of dimensions.

        """

        # `binned_statistic` requires `edges` to be at least 2d
        if kale.utils.really1d(edges):
            edges = [edges]

        # NOTE: `edges` must be increasing in each dimension!
        if np.any([np.any(np.diff(ee) < 0.0) for ee in edges]):
            raise ValueError(f"`edges` must be increasing in each dimension!  edges={edges}")

        # ---- sample grid
        # set the mass of each bin to achieve the desired `num` samples
        mass = kale.utils.trapz_dens_to_mass(data, edges)
        mass = mass * num / mass.sum()
        vv = kale.sample_grid(edges, data, mass=mass, squeeze=False)

        # ---- calculate COMs from samples
        coms = [sp.stats.binned_statistic_dd(vv.T, vv[ii], statistic='mean', bins=edges)[0] for ii in range(len(vv))]
        coms = np.asarray(coms)
        # also get the number of samples in each bin, for estimating expected accuracy
        count = sp.stats.binned_statistic_dd(vv.T, vv[0], statistic='count', bins=edges)[0]

        if np.ndim(data) == 1:
            coms = coms.squeeze()

        return coms, count

    def _general(self, shape, num=1e4):
        """Generate a random grid of data with given `shape`, and test accuracy of centroid calc.
        """
        print(f"\ngeneral shape={shape}")
        # General random bins and data of the given shape
        yy = np.random.uniform(0.0, 10.0, shape)
        xx = [sorted(np.random.uniform(0.0, 1.0, sh)) for sh in yy.shape]
        # ---- calculate the size of each bin, for measuring fractional errors
        # width of each bin, in each dimension
        dx = [np.diff(x) for x in xx]
        vol = np.meshgrid(*dx, indexing='ij')
        # find diagonal length of each bin
        vol = np.linalg.norm(vol, axis=0)
        print(f"xx={xx}")
        print(f"vol={vol}")

        # Calculate centroids using function to be tested
        coms = kale.utils.centroids(xx, yy).squeeze()
        # Calculate 'truth' value (approximation) numerically, by sampling across bins
        truth, count = self._numeric(xx, yy, num=num)

        # Flatten bins for ease for comparison
        ndim = len(xx)
        coms = np.reshape(coms, (ndim, -1))
        truth = np.reshape(truth, (ndim, -1))
        count = count.flatten()
        truth[:, (count == 0)] = 0.0
        vol = vol.flatten()
        tol = np.inf * np.ones_like(count)
        idx = (count > 0)
        tol[idx] = 3.0 * vol[idx] / np.sqrt(count[idx])
        err = np.linalg.norm(truth - coms, axis=0)

        # ---- Perform test
        print(f"coms ={coms.tolist()}")
        print(f"truth={truth.tolist()}")
        print(f"err  ={err.tolist()}")
        print(f"count={count.tolist()}")
        print(f"tol  ={tol.tolist()}")
        check = (err <= tol)
        bads = np.where(~check)
        print(f"bads={bads}")
        print(f"err[bads]={err[bads]}")
        print(f"tol[bads]={tol[bads]}")
        assert np.all(err <= tol)
        return

    def test_single_1d(self):
        """Test a few 1D single-bins"""

        # ---- Define test cases

        edges_list = [
            sorted(np.random.uniform(-1.0, 1.0, 2)),
            sorted(np.random.uniform(-10.0, 10.0, 2)),
            sorted(np.random.uniform(10.0, 100.0, 2)),
        ]

        data_list = [
            2*[np.random.uniform(0.0, 1.0)],      # uniform    yvalues
            [0.0, np.random.uniform(0.0, 2.0)],   # increasing yvalues
            [np.random.uniform(0.0, 2.0), 0.0],   # decreasing yvalues
        ]

        truth_list = [
            np.mean(edges_list[0]),
            edges_list[1][0] + (2.0/3.0) * np.diff(edges_list[1])[0],
            edges_list[2][1] - (2.0/3.0) * np.diff(edges_list[2])[0],
        ]

        # ---- Run tests

        for edges, data, truth in zip(edges_list, data_list, truth_list):
            coms = kale.utils.centroids(edges, data)
            print(f"coms={coms}  ||  for edges={edges}, data={data}")

            # test with given truth value
            print(f"\tANALYTIC: truth={truth}")
            assert np.allclose(coms, truth)

            # Test using manual/semi-analytic calculation
            truth = self._manual_single_1d(edges, data)
            print(f"\tMANUAL: truth={truth}")
            assert np.allclose(coms, truth)

            # Test using numeric/sampling calculation
            NUM = 1e4
            truth, _ = self._numeric(edges, data, num=NUM)
            err = (coms - truth) / np.fabs(np.diff(edges)[0])
            tol = 3.0 / np.sqrt(NUM)
            print(f"\tNUMERIC: truth={truth}, err={err} (told={tol}, NUM={NUM})")
            assert np.all(np.fabs(err) < tol)

        return

    def test_single_2d(self):
        """Test a few 2D single-bins"""

        # generate random bin edges and random data
        edges = [np.random.uniform(-1.0, 1.0, 2), np.random.uniform(10.0, 100.0, 2)]
        edges = [sorted(ee) for ee in edges]
        data = np.random.normal(10.0, 1.0, (2, 2))
        print(f"edges={edges}, data={data}")

        # get coms from test function
        coms = kale.utils.centroids(edges, data).squeeze()
        print(f"coms.shape={coms.shape}, coms={coms}")

        # determine true answer manually
        truth = self._manual_single_2d(edges, data).squeeze()
        print(f"truth.shape={truth.shape}")
        print(f"MANUAL: truth={truth}")
        assert np.allclose(coms, truth)

        # determine true answer numerically
        NUM = 1e4
        truth, _ = self._numeric(edges, data, num=NUM)
        truth = truth.squeeze()
        err = np.linalg.norm(np.diff(edges, axis=1))
        err = np.linalg.norm(coms - truth, axis=0) / err
        tol = 3.0 / np.sqrt(NUM)
        print(f"NUMERIC: truth={truth}, err={err}, tol={tol}")
        assert np.all(np.fabs(err) < tol)

        return

    def test_general_1d(self):
        """Test a few 1D grids, randomly generated"""
        ntests = 4
        num = 1e3
        for shape in np.random.randint(5, 20, ntests):
            self._general([shape,], num=num)
        return

    def test_general_2d(self):
        """Test a few 2D grids, randomly generated"""
        ntests = 4
        ndim = 2
        num = 1e4
        for shape in np.random.randint(3, 10, (ntests, ndim)):
            self._general(shape, num=num)
        return

    def test_general_3d(self):
        """Test a few 3D grids, randomly generated"""
        ntests = 3
        ndim = 3
        num = 1e5
        for shape in np.random.randint(3, 6, (ntests, ndim)):
            self._general(shape, num=num)
        return


class Test_Histogram(object):

    @classmethod
    def setup_class(cls):
        np.random.seed(9865)

        num_points = 20

        cls.bins = [
            13,
            np.linspace(-1.0, 1.0, 11),
        ]

        cls.data = [
            np.ones(num_points),
            np.random.uniform(-1, 1, num_points),
            np.random.poisson(size=num_points) / np.sqrt(num_points),
        ]

        cls.weights = [
            None,
            np.ones(num_points),
            np.ones(num_points) / num_points,
            np.random.uniform(0.0, 10.0, num_points),
        ]
        return

    def test_hist_dens_prob(self):
        for weights in self.weights:
            self._test_hist_dens_prob(weights)

        return

    def _test_hist_dens_prob(self, weights):
        for data in self.data:
            for bins in self.bins:
                hh, ee = utils.histogram(data, bins,
                                         weights=weights, density=True, probability=True)
                hh_true, ee_true = np.histogram(data, bins, weights=weights, density=True)

                if not np.all(ee == ee_true):
                    print("edges     = ", ee)
                    print("    truth = ", ee_true)
                    raise ValueError("Edges do not match!")

                bads = ~np.isclose(hh, hh_true)
                if np.any(bads):
                    print("hist      = ", hh)
                    print("    truth = ", hh_true)
                    raise ValueError("Histograms do not match!")

        return

    def test_hist(self):
        for weights in self.weights:
            self._test_hist(weights)

        return

    def _test_hist(self, weights):
        for data in self.data:
            for bins in self.bins:
                hh, ee = utils.histogram(data, bins,
                                         weights=weights, density=False, probability=False)
                hh_true, ee_true = np.histogram(data, bins, weights=weights, density=False)

                if not np.all(ee == ee_true):
                    print("edges     = ", ee)
                    print("    truth = ", ee_true)
                    raise ValueError("Edges do not match!")

                bads = ~np.isclose(hh, hh_true)
                if np.any(bads):
                    print("hist      = ", hh)
                    print("    truth = ", hh_true)
                    raise ValueError("Histograms do not match!")

        return

    def test_hist_dens(self):
        for weights in self.weights:
            self._test_hist_dens(weights)

        return

    def _test_hist_dens(self, weights):
        for data in self.data:
            for bins in self.bins:
                hh, ee = utils.histogram(data, bins,
                                         weights=weights, density=True, probability=False)
                hh_true, ee_true = np.histogram(data, bins, weights=weights, density=False)
                hh_true = hh_true.astype(float) / np.diff(ee_true)

                if not np.all(ee == ee_true):
                    print("edges     = ", ee)
                    print("    truth = ", ee_true)
                    raise ValueError("Edges do not match!")

                bads = ~np.isclose(hh, hh_true)
                if np.any(bads):
                    print("hist      = ", hh)
                    print("    truth = ", hh_true)
                    raise ValueError("Histograms do not match!")

        return

    def test_hist_prob(self):
        for weights in self.weights:
            self._test_hist_prob(weights)

        return

    def _test_hist_prob(self, weights):
        for data in self.data:
            for bins in self.bins:
                hh, ee = utils.histogram(data, bins,
                                         weights=weights, density=False, probability=True)
                hh_true, ee_true = np.histogram(data, bins, weights=weights, density=False)
                hh_true = hh_true.astype(float) / hh_true.sum()

                if not np.all(ee == ee_true):
                    print("edges     = ", ee)
                    print("    truth = ", ee_true)
                    raise ValueError("Edges do not match!")

                bads = ~np.isclose(hh, hh_true)
                if np.any(bads):
                    print("hist      = ", hh)
                    print("    truth = ", hh_true)
                    raise ValueError("Histograms do not match!")

        return


class Test_Midpoints(object):

    @classmethod
    def setup_class(cls):
        np.random.seed(9865)
        return

    def test_midpoints_axes(self):
        print("\n|Test_Utils:test_midpoints_axes()|")
        # NUM = 100

        shp = (12, 14, 16)
        test = np.ones(shp)
        for ii in range(test.ndim):
            vals = utils.midpoints(test, log=False, axis=ii)
            new_shape = np.array(shp)
            new_shape[ii] -= 1
            assert np.all(vals.shape == new_shape)
            assert np.all(vals == 1.0)

            vals = utils.midpoints(test, log=True, axis=ii)
            new_shape = np.array(shp)
            new_shape[ii] -= 1
            assert np.all(vals.shape == new_shape)
            assert np.all(vals == 1.0)

        test = np.arange(10)
        vals = utils.midpoints(test, log=False)
        true = 0.5 * (test[:-1] + test[1:])
        assert np.allclose(vals, true)
        return

    def test_midpoints_lin(self):
        print("\n|Test_Utils:test_midpoints_lin()|")
        test = [
            [0, 1, 2, 3],
            [2, 3, 4, 5]
        ]

        truth = [
            [1, 2, 3, 4],
            [
                [0.5, 1.5, 2.5],
                [2.5, 3.5, 4.5]
            ]
        ]

        for ii, tr in enumerate(truth):
            vals = utils.midpoints(test, log=False, axis=ii, squeeze=True)
            assert np.all(np.shape(tr) == np.shape(vals))
            assert np.all(tr == vals)

        shp = (4, 5)
        test = np.random.uniform(-1.0, 1.0, np.product(shp)).reshape(shp)
        for ii in range(2):
            vals = utils.midpoints(test, log=False, axis=ii)

            temp = np.moveaxis(test, ii, 0)
            true = temp[:-1, :] + 0.5*np.diff(temp, axis=0)
            true = np.moveaxis(true, 0, ii)
            assert np.all(np.shape(true) == np.shape(vals))
            assert np.allclose(true, vals)

        return

    def test_midpoints_log(self):
        print("\n|Test_Utils:test_midpoints_log()|")
        test = [
            [1e0, 1e1, 1e2, 1e3],
            [1e2, 1e3, 1e4, 1e5]
        ]

        aa = np.sqrt(10.0)

        truth = [
            [1e1, 1e2, 1e3, 1e4],
            [
                [aa*1e0, aa*1e1, aa*1e2],
                [aa*1e2, aa*1e3, aa*1e4]
            ]
        ]

        for ii, tr in enumerate(truth):
            vals = utils.midpoints(test, log=True, axis=ii, squeeze=True)
            assert np.all(np.shape(tr) == np.shape(vals))
            assert np.allclose(tr, vals)

        shp = (4, 5)
        test_log = np.random.uniform(-2.0, 2.0, np.product(shp)).reshape(shp)
        test_lin = 10**test_log
        for ii in range(2):
            # Make sure `midpoints` gives consistent results itself
            vals_log = utils.midpoints(test_log, log=False, axis=ii)
            vals_lin = utils.midpoints(test_lin, log=True, axis=ii)
            assert np.all(np.shape(vals_log) == np.shape(vals_lin))
            assert np.allclose(10**vals_log, vals_lin)

            # Compare log-midpoint to known values
            temp = np.moveaxis(test_lin, ii, 0)
            temp = np.log10(temp)
            true = temp[:-1, :] + 0.5*np.diff(temp, axis=0)
            true = np.moveaxis(true, 0, ii)
            true = 10**true
            assert np.all(np.shape(true) == np.shape(vals_lin))
            assert np.allclose(true, vals_lin)

        return

    def test_midpoints_off_center(self):
        print("\n|Test_Utils:test_midpoints_off_center()|")
        pass


class Test_Spacing(object):

    @classmethod
    def setup_class(cls):
        np.random.seed(1234)
        return

    def test_lin(self):
        print("\n|Test_Spacing:test_lin()|")
        aa = [64.15474369, 30.23993491, 18.74843086, 90.36893423, 81.49347391,
              21.66373546, 26.36243961,  9.54536041, 33.48985127, 87.77429238]
        bb = [9.54536041, 18.5257575, 27.5061546, 36.48655169, 45.46694878,
              54.44734587, 63.42774296, 72.40814005, 81.38853714, 90.36893423]

        test = utils.spacing(aa, 'lin', np.size(bb))
        assert np.allclose(bb, test)
        return

    def test_log(self):
        print("\n|Test_Spacing:test_log()|")
        aa = [0.56979885,  0.06782166, 38.00982397,  0.76822742,  0.24328732,
              18.22846225,  7.22905804,  0.5140395,  0.97960639, 14.57931413]
        bb = [0.06782166,  0.13701255,  0.27679121,  0.55917048,  1.12962989,
              2.28206553,  4.61020298,  9.31347996, 18.81498695, 38.00982397]

        test = utils.spacing(aa, 'log', np.size(bb))
        assert np.allclose(bb, test)
        return


class Test_Trapz(object):

    def test_1d(self):
        print("\n|Test_Trapz:test_1d()|")
        from kalepy import utils

        extr = sorted(np.random.uniform(-10, 10, 2))
        xx = np.linspace(*extr, 1000)
        yy = np.random.uniform(0.0, 1.0, xx.size)

        np_trapz = np.trapz(yy, xx)
        test = utils.trapz_nd(yy, xx)
        assert np.allclose(test, np_trapz)
        return

    def test_2d(self):
        print("\n|Test_Trapz:test_2d()|")
        from kalepy import utils
        extr = [sorted(np.random.uniform(-10, 10, 2)) for ii in range(2)]
        edges = [np.linspace(*ex, 100) for ex in extr]

        grid = np.meshgrid(*edges, indexing='ij')
        shp = np.shape(grid[0])
        vals = np.random.uniform(0.0, 1.0, size=shp)

        test = utils.trapz_nd(vals, edges)

        def sum_corner(ii, jj):
            area = np.diff(edges[0]) * np.diff(edges[1])
            temp = area * vals[ii, jj]
            return np.sum(temp)

        tot = 0.0
        for ii in range(2):
            for jj in range(2):
                cuts = []
                for kk in [ii, jj]:
                    if kk == 0:
                        cuts.append(slice(None, -1, None))
                    else:
                        cuts.append(slice(1, None, None))
                tot += sum_corner(*cuts) * 0.25

        print("test = {}, tot = {}".format(test, tot))
        assert np.allclose(test, tot)
        return

    def test_nd(self):
        print("\n|Test_Trapz:test_nd()|")

        def _test_dim(dim, num=1e7):
            from kalepy import utils

            num_per_dim = int(np.power(num, 1/dim))
            norm = np.random.normal(10.0, 1.0)
            extr = [sorted(np.random.uniform(-10, 10, 2)) for ii in range(dim)]
            edges = [np.linspace(*ex, num_per_dim) for ex in extr]

            shp = [len(ed) for ed in edges]
            vals = norm * np.ones(shp)
            tot = utils.trapz_nd(vals, edges)

            truth = np.product(np.diff(extr, axis=-1)) * norm
            print("\t{:.4e} vs {:.4e}".format(tot, truth))
            assert np.allclose(tot, truth)

            return

        for ii in range(1, 5):
            print("Dimensions: {}".format(ii))
            _test_dim(ii)

        return


# class Test_Trapz_Dens_To_Mass(utils.Test_Base):
class Test_Trapz_Dens_To_Mass:

    def _test_ndim(self, ndim):
        from kalepy import utils

        print("`ndim` = {}".format(ndim))

        BIN_SIZE_RANGE = [10, 30]

        extr = [[0.0, np.random.uniform(0.0, 2.0)] for ii in range(ndim)]
        norm = np.random.uniform(0.0, 10.0)
        # extr = [[0.0, 1.0] for ii in range(ndim)]
        # norm = 1.0

        edges = [np.linspace(*ex, np.random.randint(*BIN_SIZE_RANGE)) for ex in extr]
        grid = np.meshgrid(*edges, indexing='ij')

        lengths = np.max(extr, axis=-1)

        xx = np.min(np.moveaxis(grid, 0, -1)/lengths, axis=-1)

        pdf = norm * xx
        area = np.product(lengths)
        pmf = utils.trapz_dens_to_mass(pdf, edges)

        # Known area of a pyramid in ndim
        vol = area * norm / (ndim + 1)
        tot = np.sum(pmf)
        print("Volume = {:.4e}, Total Mass = {:.4e};  ratio = {:.4e}".format(vol, tot, tot/vol))
        assert np.allclose(vol, tot, rtol=1e-2), "total volume does not match analytic value"

        test = utils.trapz_nd(pdf, edges)
        print("Volume = {:.4e}, Total Mass = {:.4e};  ratio = {:.4e}".format(test, tot, tot/test))
        assert np.allclose(vol, tot, rtol=1e-2), "total volume does not match `trapz_nd` value"

        return

    def _test_ndim_a1(self, ndim):
        from kalepy import utils

        BIN_SIZE_RANGE = [10, 30]
        num_bins = np.random.randint(*BIN_SIZE_RANGE, ndim)
        # num_bins = [3, 4]

        edges = []
        for nb in num_bins:
            ee = np.cumsum(np.random.uniform(0.0, 2.0, nb))
            edges.append(ee)

        grid = np.meshgrid(*edges, indexing='ij')
        shp = [len(ee) for ee in edges]

        for axis in range(ndim):
            not_axis = (axis + 1) % ndim
            print("\nndim = {}, axis = {}, other = {}".format(ndim, axis, not_axis))

            bcast_norm = [np.newaxis for ii in range(ndim)]
            bcast_norm[not_axis] = slice(None)
            bcast_norm = tuple(bcast_norm)
            norm = np.random.uniform(0.0, 10.0, shp[not_axis])[bcast_norm]

            bcast_wids = [np.newaxis for ii in range(ndim)]
            bcast_wids[axis] = slice(None)
            bcast_wids = tuple(bcast_wids)
            wids = np.diff(edges[axis])[bcast_wids]

            pdf = np.ones_like(grid[0]) * norm
            pmf = utils.trapz_dens_to_mass(pdf, edges, axis=axis)

            new_shp = [ss for ss in shp]
            new_shp[axis] -= 1
            assert np.all(np.shape(pmf) == np.array(new_shp)), "Output shape is not correct"

            assert np.all(pmf == norm*wids), 'Values do not match'


        return

    def _test_ndim_a2(self, ndim):
        from kalepy import utils

        BIN_SIZE_RANGE = [10, 30]
        num_bins = np.random.randint(*BIN_SIZE_RANGE, ndim)

        edges = []
        for nb in num_bins:
            ee = np.cumsum(np.random.uniform(0.0, 2.0, nb))
            edges.append(ee)

        grid = np.meshgrid(*edges, indexing='ij')
        shp = np.array([len(ee) for ee in edges])

        for axis in np.ndindex(*([ndim]*2)):
            if len(np.unique(axis)) != len(axis):
                continue

            axis = np.asarray(axis)
            not_axis = np.array(list(set(range(ndim)) - set(axis)))
            print("\nndim = {}, axis = {}, other = {}".format(ndim, axis, not_axis))

            bcast_norm = [np.newaxis for ii in range(ndim)]
            for na in not_axis:
                bcast_norm[na] = slice(None)

            bcast_norm = tuple(bcast_norm)
            norm = np.random.uniform(0.0, 10.0, shp[not_axis])[bcast_norm]

            widths = []
            for ii in range(ndim):
                dim_len_inn = shp[ii]
                if ii in axis:
                    wid = np.diff(edges[ii])
                else:
                    wid = np.ones(dim_len_inn)

                # Create new axes along all by the current dimension, slice along the current dimension
                cut = [np.newaxis for ii in range(ndim)]
                cut[ii] = slice(None)
                temp = wid[tuple(cut)]
                widths.append(temp)

            wids = np.product(np.array(widths, dtype=object), axis=0).astype(float)

            pdf = np.ones_like(grid[0]) * norm
            pmf = utils.trapz_dens_to_mass(pdf, edges, axis=axis)

            new_shp = [ss for ss in shp]
            for aa in axis:
                new_shp[aa] -= 1

            assert np.all(np.shape(pmf) == np.array(new_shp)), "Output shape is not correct"
            assert np.all(pmf == norm*wids), "Values do not match"

        return

    def test_ndim(self):
        for ii in range(1, 5):
            self._test_ndim(ii)
        return

    def test_ndim_a1(self):
        for ii in range(2, 5):
            self._test_ndim_a1(ii)
        return

    def test_ndim_a2(self):
        for ii in range(3, 5):
            self._test_ndim_a2(ii)
        return


# class Test_Cumsum(utils.Test_Base):
class Test_Cumsum:

    def _brute_force_cumsum(self, vals):
        """Brute-force cumulative sum calculation as comparison
        """
        # Make sure input is array to allow tuple-slicing
        vals = np.asarray(vals)
        # Output values
        res = np.zeros_like(vals)
        # Iterate over each input element
        for ii in np.ndindex(np.shape(vals)):
            # Sum all input elements with lower indices
            #   Add one to the current index so that we count them inclusively
            kk = np.array(ii) + 1
            for jj in np.ndindex(tuple(kk)):
                res[ii] += vals[jj]

        return res

    def _test_no_axis_ndim(self, ndim):
        """Test cumsum over all axes (i.e. "no" axis given) for a `ndim` array
        """
        # Construct a random shape in `ndim` dimensions
        shape = np.random.randint(2, 7, ndim)
        # Fill with random values
        vals = np.random.uniform(-20.0, 20.0, shape)

        # Get the `cumsum` result
        res = utils.cumsum(vals)
        # Get the brute-force result for comparison
        chk = self._brute_force_cumsum(vals)
        # Make sure they match
        print("input = \n", vals)
        print("output = \n", res)
        print("brute-force truth = \n", chk)
        msg = "cumsum ndim={} does not match brute-force values.".format(ndim)
        assert np.allclose(res, chk, rtol=1e-10), msg
        return

    def _test_axis_ndim(self, ndim, axis):
        """Test cumsum over particular axis for a `ndim` array
        """
        # Construct a random shape in `ndim` dimensions
        shape = np.random.randint(2, 7, ndim)
        # Fill with random values
        vals = np.random.uniform(-20.0, 20.0, shape)

        # Get the `cumsum` result
        res = utils.cumsum(vals, axis=axis)
        # Get the brute-force result for comparison
        # chk = self._brute_force_cumsum(vals)
        chk = np.cumsum(vals, axis=axis)
        # Make sure they match
        print("input = \n", vals)
        print("output = \n", res)
        print("numpy truth = \n", chk)
        msg = "cumsum ndim={}, axis={} does not match brute-force values.".format(ndim, axis)
        assert np.allclose(res, chk, rtol=1e-10), msg
        return

    def test_no_axis(self):
        # Start with a known input and output
        test = [[1, 2, 3, 4],
                [0, 2, 1, 2],
                [3, 1, 0, 0]]
        check = [[1, 3, 6, 10],
                 [1, 5, 9, 15],
                 [4, 9, 13, 19]]
        res = utils.cumsum(test)
        print("input = \n", test)
        print("output = \n", res)
        print("brute-force truth = \n", check)
        assert np.allclose(res, check, rtol=1e-10), "`cumsum` does not match known result"

        for nd in range(1, 5):
            self._test_no_axis_ndim(nd)

        return

    def test_axis(self):
        """With axis given, this just needs to match `numpy.cumsum` results.
        """
        # Start with a known input and output
        test = [[1, 2, 3, 4],
                [0, 2, 1, 2],
                [3, 1, 0, 0]]
        chk_a1 = [[1, 3, 6, 10],
                  [0, 2, 3, 5],
                  [3, 4, 4, 4]]
        chk_a0 = [[1, 2, 3, 4],
                  [1, 4, 4, 6],
                  [4, 5, 4, 6]]

        checks = [chk_a0, chk_a1]
        print("input = \n", test)
        for aa, chk in enumerate(checks):
            print("---- axis=", aa)
            res = utils.cumsum(test, axis=aa)
            chk_np = np.cumsum(test, axis=aa)
            print("output = \n", res)
            print("numpy truth = \n", chk_np)
            msg = "`cumsum` does not match numpy result along axis={}".format(aa)
            assert np.allclose(res, chk_np, rtol=1e-10), msg

            print("output = \n", res)
            print("brute-force truth = \n", chk)
            msg = "`cumsum` does not match known result along axis={}".format(aa)
            assert np.allclose(res, chk, rtol=1e-10), msg

        for nd in range(1, 5):
            for ax in range(nd):
                self._test_axis_ndim(nd, ax)

        return


# class Test_Really1D(utils.Test_Base):
class Test_Really1D:

    def _test_vals(self, vals, truth):
        print("`vv` should be: {} :: shape = {} :: '{}'".format(truth, utils.jshape(vals), vals))
        assert utils.really1d(vals) == truth
        return

    def test_1d_true(self):
        vals = [
            [],
            [0],
            [None],
            [1, 2, 3],
            np.arange(10),
            np.array([]),
            np.array([5]),
        ]

        for vv in vals:
            self._test_vals(vv, True)

        return

    def test_0d_false(self):
        vals = [
            0,
            None,
            np.array(None),
            np.array(-5),
        ]

        for vv in vals:
            self._test_vals(vv, False)

        return

    def test_2d_false(self):
        vals = [
            np.arange(12).reshape(4, 3),
            [[0, 1], [1, 2]],
            [[1, 2, 3]],
            [np.arange(10)],
            # Jagged
            [[1], [2, 3]],
            [[], [1]],
            [None, [1, 3]],
        ]

        for vv in vals:
            self._test_vals(vv, False)

        return
