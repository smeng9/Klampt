# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""Python interface to C++ motion planning routines"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _motionplanning
else:
    import _motionplanning

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _motionplanning.delete_SwigPyIterator

    def value(self):
        return _motionplanning.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _motionplanning.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _motionplanning.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _motionplanning.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _motionplanning.SwigPyIterator_equal(self, x)

    def copy(self):
        return _motionplanning.SwigPyIterator_copy(self)

    def next(self):
        return _motionplanning.SwigPyIterator_next(self)

    def __next__(self):
        return _motionplanning.SwigPyIterator___next__(self)

    def previous(self):
        return _motionplanning.SwigPyIterator_previous(self)

    def advance(self, n):
        return _motionplanning.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _motionplanning.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _motionplanning.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _motionplanning.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _motionplanning.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _motionplanning.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _motionplanning.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _motionplanning:
_motionplanning.SwigPyIterator_swigregister(SwigPyIterator)

class doubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _motionplanning.doubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _motionplanning.doubleVector___nonzero__(self)

    def __bool__(self):
        return _motionplanning.doubleVector___bool__(self)

    def __len__(self):
        return _motionplanning.doubleVector___len__(self)

    def __getslice__(self, i, j):
        return _motionplanning.doubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _motionplanning.doubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _motionplanning.doubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _motionplanning.doubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _motionplanning.doubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _motionplanning.doubleVector___setitem__(self, *args)

    def pop(self):
        return _motionplanning.doubleVector_pop(self)

    def append(self, x):
        return _motionplanning.doubleVector_append(self, x)

    def empty(self):
        return _motionplanning.doubleVector_empty(self)

    def size(self):
        return _motionplanning.doubleVector_size(self)

    def swap(self, v):
        return _motionplanning.doubleVector_swap(self, v)

    def begin(self):
        return _motionplanning.doubleVector_begin(self)

    def end(self):
        return _motionplanning.doubleVector_end(self)

    def rbegin(self):
        return _motionplanning.doubleVector_rbegin(self)

    def rend(self):
        return _motionplanning.doubleVector_rend(self)

    def clear(self):
        return _motionplanning.doubleVector_clear(self)

    def get_allocator(self):
        return _motionplanning.doubleVector_get_allocator(self)

    def pop_back(self):
        return _motionplanning.doubleVector_pop_back(self)

    def erase(self, *args):
        return _motionplanning.doubleVector_erase(self, *args)

    def __init__(self, *args):
        _motionplanning.doubleVector_swiginit(self, _motionplanning.new_doubleVector(*args))

    def push_back(self, x):
        return _motionplanning.doubleVector_push_back(self, x)

    def front(self):
        return _motionplanning.doubleVector_front(self)

    def back(self):
        return _motionplanning.doubleVector_back(self)

    def assign(self, n, x):
        return _motionplanning.doubleVector_assign(self, n, x)

    def resize(self, *args):
        return _motionplanning.doubleVector_resize(self, *args)

    def insert(self, *args):
        return _motionplanning.doubleVector_insert(self, *args)

    def reserve(self, n):
        return _motionplanning.doubleVector_reserve(self, n)

    def capacity(self):
        return _motionplanning.doubleVector_capacity(self)
    __swig_destroy__ = _motionplanning.delete_doubleVector

# Register doubleVector in _motionplanning:
_motionplanning.doubleVector_swigregister(doubleVector)

class doubleMatrix(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _motionplanning.doubleMatrix_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _motionplanning.doubleMatrix___nonzero__(self)

    def __bool__(self):
        return _motionplanning.doubleMatrix___bool__(self)

    def __len__(self):
        return _motionplanning.doubleMatrix___len__(self)

    def __getslice__(self, i, j):
        return _motionplanning.doubleMatrix___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _motionplanning.doubleMatrix___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _motionplanning.doubleMatrix___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _motionplanning.doubleMatrix___delitem__(self, *args)

    def __getitem__(self, *args):
        return _motionplanning.doubleMatrix___getitem__(self, *args)

    def __setitem__(self, *args):
        return _motionplanning.doubleMatrix___setitem__(self, *args)

    def pop(self):
        return _motionplanning.doubleMatrix_pop(self)

    def append(self, x):
        return _motionplanning.doubleMatrix_append(self, x)

    def empty(self):
        return _motionplanning.doubleMatrix_empty(self)

    def size(self):
        return _motionplanning.doubleMatrix_size(self)

    def swap(self, v):
        return _motionplanning.doubleMatrix_swap(self, v)

    def begin(self):
        return _motionplanning.doubleMatrix_begin(self)

    def end(self):
        return _motionplanning.doubleMatrix_end(self)

    def rbegin(self):
        return _motionplanning.doubleMatrix_rbegin(self)

    def rend(self):
        return _motionplanning.doubleMatrix_rend(self)

    def clear(self):
        return _motionplanning.doubleMatrix_clear(self)

    def get_allocator(self):
        return _motionplanning.doubleMatrix_get_allocator(self)

    def pop_back(self):
        return _motionplanning.doubleMatrix_pop_back(self)

    def erase(self, *args):
        return _motionplanning.doubleMatrix_erase(self, *args)

    def __init__(self, *args):
        _motionplanning.doubleMatrix_swiginit(self, _motionplanning.new_doubleMatrix(*args))

    def push_back(self, x):
        return _motionplanning.doubleMatrix_push_back(self, x)

    def front(self):
        return _motionplanning.doubleMatrix_front(self)

    def back(self):
        return _motionplanning.doubleMatrix_back(self)

    def assign(self, n, x):
        return _motionplanning.doubleMatrix_assign(self, n, x)

    def resize(self, *args):
        return _motionplanning.doubleMatrix_resize(self, *args)

    def insert(self, *args):
        return _motionplanning.doubleMatrix_insert(self, *args)

    def reserve(self, n):
        return _motionplanning.doubleMatrix_reserve(self, n)

    def capacity(self):
        return _motionplanning.doubleMatrix_capacity(self)
    __swig_destroy__ = _motionplanning.delete_doubleMatrix

# Register doubleMatrix in _motionplanning:
_motionplanning.doubleMatrix_swigregister(doubleMatrix)


def setRandomSeed(seed):
    r"""
    Sets the random seed used by the configuration sampler.  

    Args:
        seed (int)
    """
    return _motionplanning.setRandomSeed(seed)

def setPlanJSONString(string):
    r"""
    Loads planner values from a JSON string.  

    Args:
        string (str)
    """
    return _motionplanning.setPlanJSONString(string)

def getPlanJSONString():
    r"""
    Saves planner values to a JSON string.  

    Returns:
        str:
    """
    return _motionplanning.getPlanJSONString()

def setPlanType(type):
    r"""
    Sets the planner type.  

    Args:
        type (str)

    Valid values are  

    *   prm: the Probabilistic Roadmap algorithm  
    *   rrt: the Rapidly Exploring Random Trees algorithm  
    *   sbl: the Single-Query Bidirectional Lazy planner  
    *   sblprt: the probabilistic roadmap of trees (PRT) algorithm with SBL as the
        inter-root planner.  
    *   rrt*: the RRT* algorithm for optimal motion planning  
    *   prm*: the PRM* algorithm for optimal motion planning  
    *   lazyprm*: the Lazy-PRM* algorithm for optimal motion planning  
    *   lazyrrg*: the Lazy-RRG* algorithm for optimal motion planning  
    *   fmm: the fast marching method algorithm for resolution-complete optimal
        motion planning  
    *   fmm*: an anytime fast marching method algorithm for optimal motion planning  

    """
    return _motionplanning.setPlanType(type)

def setPlanSetting(*args):
    r"""
    Sets a numeric or string-valued setting for the planner.  

    setPlanSetting (setting,value)


    Args:
        setting (str): 
        value (str or float): 

    Valid numeric values are:  

    *   "knn": k value for the k-nearest neighbor connection strategy (only for
        PRM)  
    *   "connectionThreshold": a milestone connection threshold  
    *   "perturbationRadius": (for RRT and SBL)  
    *   "bidirectional": 1 if bidirectional planning is requested (for RRT)  
    *   "grid": 1 if a point selection grid should be used (for SBL)  
    *   "gridResolution": resolution for the grid, if the grid should be used (for
        SBL with grid, FMM, FMM*)  
    *   "suboptimalityFactor": allowable suboptimality (for RRT*, lazy PRM*, lazy
        RRG*)  
    *   "randomizeFrequency": a grid randomization frequency (for SBL)  
    *   "shortcut": nonzero if you wish to perform shortcutting after a first plan
        is found.  
    *   "restart": nonzero if you wish to restart the planner to get better paths
        with the remaining time.  

    Valid string values are:  

    *   "pointLocation": a string designating a point location data structure.
        "kdtree" is supported, optionally followed by a weight vector (for PRM,
        RRT*, PRM*, LazyPRM*, LazyRRG*)  
    *   "restartTermCond": used if the "restart" setting is true. This is a JSON
        string defining the termination condition.  

        The default value is "{foundSolution:1;maxIters:1000}", which indicates
        that the planner will restart if it has found a solution, or 1000 iterations
        have passed.  

        To restart after a certain amount of time has elasped, use
        "{timeLimit:X}". If you are using an optimizing planner, e.g.,
        shortcutting, you should set foundSolution:0.  

    """
    return _motionplanning.setPlanSetting(*args)

def destroy():
    r"""
    destroys internal data structures  

    """
    return _motionplanning.destroy()
class CSpaceInterface(object):
    r"""


    A raw interface for a configuration space. Note: the native Python CSpace
    interface class in cspace.py is easier to use.  

    You can either set a single feasibility test function using setFeasibility() or
    add several feasibility tests, all of which need to be satisfied, using
    addFeasibilityTest(). In the latter case, planners may be able to provide
    debugging statistics, solve Minimum Constraint Removal problems, run faster by
    eliminating constraint tests, etc.  

    Either setVisibility() or setVisibilityEpsilon() must be called to define a
    visibility checker between two (feasible) configurations. In the latter case,
    the path will be discretized at the resolution sent to setVisibilityEpsilon. If
    you have special single-constraint visibility tests, you can call that using
    addVisibilityTest (for example, for convex constraints you can set it to the
    lambda function that returns true regardless of its arguments).  

    Supported properties include "euclidean" (boolean), "metric" (string),
    "geodesic" (boolean), "minimum" (vector), and "maximum" (vector). These
    may be used by planners to make planning faster or more accurate. For a complete
    list see KrisLibrary/planning/CSpace.h.  

    C++ includes: motionplanning.h

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__ (): :class:`~klampt.CSpaceInterface`

        __init__ (arg2): :class:`~klampt.CSpaceInterface`


        Args:
            arg2 (:class:`~klampt.CSpaceInterface`, optional): 
        """
        _motionplanning.CSpaceInterface_swiginit(self, _motionplanning.new_CSpaceInterface(*args))
    __swig_destroy__ = _motionplanning.delete_CSpaceInterface

    def destroy(self):
        r"""
        """
        return _motionplanning.CSpaceInterface_destroy(self)

    def setFeasibility(self, pyFeas):
        r"""
        Args:
            pyFeas (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_setFeasibility(self, pyFeas)

    def addFeasibilityTest(self, name, pyFeas):
        r"""
        Args:
            name (str)
            pyFeas (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_addFeasibilityTest(self, name, pyFeas)

    def setVisibility(self, pyVisible):
        r"""
        Args:
            pyVisible (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_setVisibility(self, pyVisible)

    def addVisibilityTest(self, name, pyVisible):
        r"""
        Args:
            name (str)
            pyVisible (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_addVisibilityTest(self, name, pyVisible)

    def setVisibilityEpsilon(self, eps):
        r"""
        Args:
            eps (float)
        """
        return _motionplanning.CSpaceInterface_setVisibilityEpsilon(self, eps)

    def setSampler(self, pySamp):
        r"""
        Args:
            pySamp (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_setSampler(self, pySamp)

    def setNeighborhoodSampler(self, pySamp):
        r"""
        Args:
            pySamp (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_setNeighborhoodSampler(self, pySamp)

    def setDistance(self, pyDist):
        r"""
        Args:
            pyDist (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_setDistance(self, pyDist)

    def setInterpolate(self, pyInterp):
        r"""
        Args:
            pyInterp (:obj:`PyObject *`)
        """
        return _motionplanning.CSpaceInterface_setInterpolate(self, pyInterp)

    def setProperty(self, key, value):
        r"""
        Args:
            key (str)
            value (str)
        """
        return _motionplanning.CSpaceInterface_setProperty(self, key, value)

    def getProperty(self, key):
        r"""
        Args:
            key (str)
        Returns:
            str:
        """
        return _motionplanning.CSpaceInterface_getProperty(self, key)

    def isFeasible(self, q):
        r"""
        Queries whether a given configuration is feasible.  

        Args:
            q (:obj:`PyObject *`)
        Returns:
            bool:
        """
        return _motionplanning.CSpaceInterface_isFeasible(self, q)

    def isVisible(self, a, b):
        r"""
        Queries whether two configurations are visible.  

        Args:
            a (:obj:`PyObject *`)
            b (:obj:`PyObject *`)
        Returns:
            bool:
        """
        return _motionplanning.CSpaceInterface_isVisible(self, a, b)

    def testFeasibility(self, name, q):
        r"""
        Queries whether a given configuration is feasible with respect to a given
        constraint.  

        Args:
            name (str)
            q (:obj:`PyObject *`)
        Returns:
            bool:
        """
        return _motionplanning.CSpaceInterface_testFeasibility(self, name, q)

    def testVisibility(self, name, a, b):
        r"""
        Queries whether two configurations are visible with respect to a given
        constraint.  

        Args:
            name (str)
            a (:obj:`PyObject *`)
            b (:obj:`PyObject *`)
        Returns:
            bool:
        """
        return _motionplanning.CSpaceInterface_testVisibility(self, name, a, b)

    def feasibilityFailures(self, q):
        r"""
        Returns a list of all failed feasibility constraints.  

        Args:
            q (:obj:`PyObject *`)
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_feasibilityFailures(self, q)

    def visibilityFailures(self, a, b):
        r"""
        Returns a list of all failed visibility constraints.  

        Args:
            a (:obj:`PyObject *`)
            b (:obj:`PyObject *`)
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_visibilityFailures(self, a, b)

    def sample(self):
        r"""
        Samples a configuration.  

        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_sample(self)

    def distance(self, a, b):
        r"""
        Returns the distance between two configurations.  

        Args:
            a (:obj:`PyObject *`)
            b (:obj:`PyObject *`)
        Returns:
            float:
        """
        return _motionplanning.CSpaceInterface_distance(self, a, b)

    def interpolate(self, a, b, u):
        r"""
        Interpolates between two configurations.  

        Args:
            a (:obj:`PyObject *`)
            b (:obj:`PyObject *`)
            u (float)
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_interpolate(self, a, b, u)

    def adaptiveQueriesEnabled(self):
        r"""
        optional: adaptive queries can be used to automatically minimize the total cost
        of testing feasibility / visibility using empirical estimates. Off by default.  

        Returns:
            bool:
        """
        return _motionplanning.CSpaceInterface_adaptiveQueriesEnabled(self)

    def enableAdaptiveQueries(self, enabled=True):
        r"""
        Call this to enable adaptive queries. (It has a small overhead.)  

        Args:
            enabled (bool, optional): default value True
        """
        return _motionplanning.CSpaceInterface_enableAdaptiveQueries(self, enabled)

    def optimizeQueryOrder(self):
        r"""
        Call this to optimize the feasibility / visibility testing order.  

        """
        return _motionplanning.CSpaceInterface_optimizeQueryOrder(self)

    def setFeasibilityDependency(self, name, precedingTest):
        r"""
        Marks that a certain feasibility test must be performed before another.  

        Args:
            name (str)
            precedingTest (str)
        """
        return _motionplanning.CSpaceInterface_setFeasibilityDependency(self, name, precedingTest)

    def setFeasibilityPrior(self, name, costPrior=0.0, feasibilityProbability=0.0, evidenceStrength=1.0):
        r"""
        Resets the data for a certain feasibility test. Default values give a data-
        gathering behavior.  

        Args:
            name (str)
            costPrior (float, optional): default value 0.0
            feasibilityProbability (float, optional): default value 0.0
            evidenceStrength (float, optional): default value 1.0
        """
        return _motionplanning.CSpaceInterface_setFeasibilityPrior(self, name, costPrior, feasibilityProbability, evidenceStrength)

    def setVisibilityDependency(self, name, precedingTest):
        r"""
        Marks that a certain feasibility test must be performed before another.  

        Args:
            name (str)
            precedingTest (str)
        """
        return _motionplanning.CSpaceInterface_setVisibilityDependency(self, name, precedingTest)

    def setVisibilityPrior(self, name, costPrior=0.0, visibilityProbability=0.0, evidenceStrength=1.0):
        r"""
        Resets the data for a certain visibility test. Default values give a data-
        gathering behavior.  

        Args:
            name (str)
            costPrior (float, optional): default value 0.0
            visibilityProbability (float, optional): default value 0.0
            evidenceStrength (float, optional): default value 1.0
        """
        return _motionplanning.CSpaceInterface_setVisibilityPrior(self, name, costPrior, visibilityProbability, evidenceStrength)

    def feasibilityCost(self, name):
        r"""
        Retrieves the empirical average cost of a given feasibility test.  

        Args:
            name (str)
        Returns:
            float:
        """
        return _motionplanning.CSpaceInterface_feasibilityCost(self, name)

    def feasibilityProbability(self, name):
        r"""
        Retrieves the empirical average success rate of a given feasibility test.  

        Args:
            name (str)
        Returns:
            float:
        """
        return _motionplanning.CSpaceInterface_feasibilityProbability(self, name)

    def visibilityCost(self, name):
        r"""
        Retrieves the empirical average cost of a given visibility test.  

        Args:
            name (str)
        Returns:
            float:
        """
        return _motionplanning.CSpaceInterface_visibilityCost(self, name)

    def visibilityProbability(self, name):
        r"""
        Retrieves the empirical average success rate of a given visibility test.  

        Args:
            name (str)
        Returns:
            float:
        """
        return _motionplanning.CSpaceInterface_visibilityProbability(self, name)

    def feasibilityQueryOrder(self):
        r"""
        Retrieves the current order of feasibility tests.  

        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_feasibilityQueryOrder(self)

    def visibilityQueryOrder(self):
        r"""
        Retrieves the current order of visibility tests.  

        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_visibilityQueryOrder(self)

    def getStats(self):
        r"""
        Returns constraint testing statistics. If adaptive queries are enabled, this
        returns the stats on each constraint.  

        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.CSpaceInterface_getStats(self)
    index = property(_motionplanning.CSpaceInterface_index_get, _motionplanning.CSpaceInterface_index_set, doc=r"""index : int""")

# Register CSpaceInterface in _motionplanning:
_motionplanning.CSpaceInterface_swigregister(CSpaceInterface)

class PlannerInterface(object):
    r"""


    An interface for a kinematic motion planner. The :class:`MotionPlan` interface
    in cspace.py is somewhat easier to use.  

    On construction, uses the planner type specified by setPlanType and the settings
    currently specified by calls to setPlanSetting.  

    Point-to-point planning is enabled by sending two configurations to the
    setEndpoints method. This is mandatory for RRT and SBL-style planners. The start
    and end milestones are given by indices 0 and 1, respectively  

    Point-to-set planning is enabled by sending a *goal test* as the second argument
    to the setEndpoints method. It is possible also to send a special goal sampler
    by providing a *pair of functions* as the second argument consisting of the two
    functions (goaltest,goalsample). The first in this pair tests whether a
    configuration is a goal, and the second returns a sampled configuration in a
    superset of the goal. Ideally the goal sampler generates as many goals as
    possible.  

    To plan, call planMore(iters) until getPath(0,1) returns non-NULL. The return
    value is a list of configurations.  

    Some planners can be used multi-query mode (such as PRM). In multi-query mode,
    you may call addMilestone(q) to add a new milestone. addMilestone() returns the
    index of that milestone, which can be used in later calls to getPath().  

    In point-to-set mode, getSolutionPath will return the optimal path to any goal
    milestone.  

    All planners work with the standard path-length objective function. Some
    planners can work with other cost functions, and you can use setCostFunction to
    set the edge / terminal costs. Usually, the results will only be optimal on the
    computed graph, and the graph is not specifically computed to optimize that
    cost.  

    To get a roadmap (V,E), call getRoadmap(). V is a list of configurations (each
    configuration is a Python list) and E is a list of edges (each edge is a pair
    (i,j) indexing into V).  

    To dump the roadmap to disk, call dump(fn). This saves to a Trivial Graph Format
    (TGF) format.  

    C++ includes: motionplanning.h

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, cspace):
        r"""
        Args:
            cspace (:class:`~klampt.CSpaceInterface`)
        """
        _motionplanning.PlannerInterface_swiginit(self, _motionplanning.new_PlannerInterface(cspace))
    __swig_destroy__ = _motionplanning.delete_PlannerInterface

    def destroy(self):
        r"""
        """
        return _motionplanning.PlannerInterface_destroy(self)

    def setEndpoints(self, start, goal):
        r"""
        Args:
            start (:obj:`PyObject *`)
            goal (:obj:`PyObject *`)
        Returns:
            bool:
        """
        return _motionplanning.PlannerInterface_setEndpoints(self, start, goal)

    def setEndpointSet(self, start, goal, goalSample=None):
        r"""
        Args:
            start (:obj:`PyObject *`)
            goal (:obj:`PyObject *`)
            goalSample (:obj:`PyObject *`, optional): default value None
        Returns:
            bool:
        """
        return _motionplanning.PlannerInterface_setEndpointSet(self, start, goal, goalSample)

    def setCostFunction(self, edgeCost=None, terminalCost=None):
        r"""
        Args:
            edgeCost (:obj:`PyObject *`, optional): default value None
            terminalCost (:obj:`PyObject *`, optional): default value None
        """
        return _motionplanning.PlannerInterface_setCostFunction(self, edgeCost, terminalCost)

    def addMilestone(self, milestone):
        r"""
        Args:
            milestone (:obj:`PyObject *`)
        Returns:
            int:
        """
        return _motionplanning.PlannerInterface_addMilestone(self, milestone)

    def getClosestMilestone(self, config):
        r"""
        Args:
            config (:obj:`PyObject *`)
        Returns:
            int:
        """
        return _motionplanning.PlannerInterface_getClosestMilestone(self, config)

    def getMilestone(self, arg2):
        r"""
        Args:
            arg2 (int)
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.PlannerInterface_getMilestone(self, arg2)

    def planMore(self, iterations):
        r"""
        Args:
            iterations (int)
        """
        return _motionplanning.PlannerInterface_planMore(self, iterations)

    def getSolutionPath(self):
        r"""
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.PlannerInterface_getSolutionPath(self)

    def getPath(self, *args):
        r"""
        getPath (milestone1,milestone2): :obj:`object`

        getPath (milestone1,int,goalMilestones): :obj:`PyObject *`


        Args:
            milestone1 (int): 
            milestone2 (int, optional): 
            int (:obj:`std::vector<`, optional): 
            goalMilestones (:obj:`std::allocator< int > >`, optional): 

        Returns:
            (:obj:`PyObject *` or :obj:`object`):
        """
        return _motionplanning.PlannerInterface_getPath(self, *args)

    def getData(self, setting):
        r"""
        Args:
            setting (str)
        Returns:
            float:
        """
        return _motionplanning.PlannerInterface_getData(self, setting)

    def getStats(self):
        r"""
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.PlannerInterface_getStats(self)

    def getRoadmap(self):
        r"""
        Returns:
            :obj:`PyObject *`:
        """
        return _motionplanning.PlannerInterface_getRoadmap(self)

    def dump(self, fn):
        r"""
        Args:
            fn (str)
        """
        return _motionplanning.PlannerInterface_dump(self, fn)
    index = property(_motionplanning.PlannerInterface_index_get, _motionplanning.PlannerInterface_index_set, doc=r"""index : int""")
    spaceIndex = property(_motionplanning.PlannerInterface_spaceIndex_get, _motionplanning.PlannerInterface_spaceIndex_set, doc=r"""spaceIndex : int""")

# Register PlannerInterface in _motionplanning:
_motionplanning.PlannerInterface_swigregister(PlannerInterface)


def interpolate1DMinTime(x0, v0, x1, v1, xmin, xmax, vmax, amax):
    r"""interpolate1DMinTime(double x0, double v0, double x1, double v1, double xmin, double xmax, double vmax, double amax)"""
    return _motionplanning.interpolate1DMinTime(x0, v0, x1, v1, xmin, xmax, vmax, amax)

def interpolate1DMinAccel(x0, v0, x1, v1, endTime, xmin, xmax, vmax):
    r"""interpolate1DMinAccel(double x0, double v0, double x1, double v1, double endTime, double xmin, double xmax, double vmax)"""
    return _motionplanning.interpolate1DMinAccel(x0, v0, x1, v1, endTime, xmin, xmax, vmax)

def interpolateNDMinTime(x0, v0, x1, v1, xmin, xmax, vmax, amax):
    r"""interpolateNDMinTime(doubleVector x0, doubleVector v0, doubleVector x1, doubleVector v1, doubleVector xmin, doubleVector xmax, doubleVector vmax, doubleVector amax)"""
    return _motionplanning.interpolateNDMinTime(x0, v0, x1, v1, xmin, xmax, vmax, amax)

def interpolateNDMinAccel(x0, v0, x1, v1, endTime, xmin, xmax, vmax):
    r"""interpolateNDMinAccel(doubleVector x0, doubleVector v0, doubleVector x1, doubleVector v1, double endTime, doubleVector xmin, doubleVector xmax, doubleVector vmax)"""
    return _motionplanning.interpolateNDMinAccel(x0, v0, x1, v1, endTime, xmin, xmax, vmax)

def interpolateNDMinTimeLinear(x0, x1, vmax, amax):
    r"""interpolateNDMinTimeLinear(doubleVector x0, doubleVector x1, doubleVector vmax, doubleVector amax)"""
    return _motionplanning.interpolateNDMinTimeLinear(x0, x1, vmax, amax)

def combineNDCubic(times, positions, velocities):
    r"""combineNDCubic(doubleMatrix times, doubleMatrix positions, doubleMatrix velocities)"""
    return _motionplanning.combineNDCubic(times, positions, velocities)


