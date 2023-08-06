/*
Compile with:
c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup -I/Library/Frameworks/Python.framework/Headers -I"/Users/diego.pedregal/Google Drive/C++/armadillo-10.8.2/include" -llapack -lblas $(python3 -m pybind11 --includes) pythonUComp.cpp -o UCc$(python3-config --extension-suffix)
*/
#include "BSMmodel.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
//#include <pybind11/pytypes.h>
namespace py = pybind11;

class BSMreturn{       // The class
  public:             // Access specifier
//    string model, compNames;
//    vector<double> p, yFor, yForV, ySimul, comp;
//    vector<string> table;
    vector<double> p, p0, yFor, periods, rhos, yForV, betaAug, betaAugVar, criteria,
                   grad, constPar, typePar, ns, nPar, harmonics, cycleLimits, u,
                   typeOutliers, coef, a, P, v, F, yFit, eps, eta, comp, compV;
    string model, estimOk, stateNames, compNames;
    int nonStationaryTerms, d_t, h, iter, rowc, rowu, rowtype, rowa, rowP, roweta, rowcomp;
    double innVariance, objFunValue, outlier, lambdaBoxCox;
    vector<string> table;
};

BSMreturn UCfunC(string command, vector<double> ys, vector<double> us, int rowu, int colu,
	             string model, vector<double> periodss, vector<double> rhoss,
	             int h, bool tTest, string criterion, vector<double> ps,
	             bool verbose, bool stepwise, string estimOk, vector<double> p0s,
	             vector<double> vs, vector<double> yFitVs, int nonStationaryTerms,
	             vector<double> harmonicss, vector<double> criterias, vector<double> betass,
	             vector<double> betaVs, int d_t, double innVariance, double objFunValue,
	             double outlier, bool arma, int Iter, int seas, vector<double> grads,
	             vector<double> constPars, vector<double> typePars, vector<double> nss,
	             vector<double> nPars, vector<double> cycleLimitss, int rowc,
	             vector<double> typeOutlierss, int rowtype, bool MSOE, bool PTSnames, 
                 double lambdaBoxCox, vector<double> TVPs,
                 string trendOptions, string seasonalOptions, string irregularOptions){
   // Transforming inputs into armadillo format
    vec y = ys;
    mat u;
    vec aux;
    if (rowu > 0){
         aux = us;
         u = reshape(aux, colu, rowu);
         u = u.t();
    }
    vec periods = periodss;
    vec rhos = rhoss;
    vec p = ps;
    vec p0 = p0s;
    vec v = vs;
    vec yFitV = yFitVs;
    vec harmonics = harmonicss;
    vec criteria = criterias;
    vec betas = betass;
    vec betaV = betaVs;
    vec grad = grads;
    vec constPar = constPars;
    vec typePar = typePars;
    vec ns = nss;
    vec nPar = nPars;
    vec TVP = TVPs;
    mat cycleLimits;
    aux = cycleLimitss;
    cycleLimits = reshape(aux, rowc, 2);
    mat typeOutliers;
    aux = typeOutlierss;
    typeOutliers = reshape(aux, rowtype, 2);
    // End of inputs

    // Correcting dimensions of u (k x n)
    size_t k = u.n_rows;
    size_t n = u.n_cols;
    mat up(k,n);
    mat typeOutliersp(typeOutliers.n_rows,typeOutliers.n_cols);
    up=u;
    typeOutliersp=typeOutliers;
    if (k > n){
        up = up.t();
    }
    if (k == 1 && n == 2){
        up.resize(0);
    }
    if (typeOutliers(0, 0) == -1){
        typeOutliersp.reset();
    }
//     if (k > n){
//         u = u.t();
//     }
//     printf("%s", "line 99\n");
//     if (k == 1 && n == 2){
//         printf("%s", "inside if 103");
//         u.reset();
//         printf("%s", "inside if 105 after reset()");
//     }
//     u.print("u 105");
//     printf("%s", "line 103\n");
//     if (typeOutliers(0, 0) == -1){
//         typeOutliers.reset();
//     }
//     printf("%s", "line 107\n");
//     periods.print("periods 108");
    //double outlier = rubbish(4);
    vec pp(2); pp(0) = periods.n_elem * 2 + 2; pp(1) = sum(ns);
    int iniObs = max(pp);
    //int iniObs;
    // Setting inputs
    SSinputs inputsSS;
    BSMmodel inputsBSM;
    // Pre-processing
    bool errorExit = preProcess(y, up, model, h, outlier, criterion, periods, p0, iniObs,
                                trendOptions, seasonalOptions, irregularOptions, TVP, lambdaBoxCox);
    BSMreturn m1;
    if (errorExit){    // ERROR
            m1.model = "error";
            return m1;
    }
//    if (errorExit){
//        string model = "error";
//        plhs[2] = mxCreateString(model.c_str());
//        armaSetPr(plhs[2],model);
//        return;
//    }
    // End of pre-processing
    if (command == "estimate"){
        inputsSS.y = y.rows(iniObs, y.n_elem - 1);
    } else {
        inputsSS.y = y;
    }
    mat uIni;
    if (iniObs > 0 && up.n_rows > 0 && command == "estimate"){
        inputsSS.u = up.cols(iniObs, up.n_cols - 1);
        uIni = up.cols(0, iniObs - 1);
    } else {
        inputsSS.u= up;
    }
    inputsBSM.model = model;
    inputsBSM.periods = periods;
    inputsBSM.rhos = rhos;
    inputsSS.h = h;
    inputsBSM.tTest = tTest;
    inputsBSM.criterion = criterion;
    inputsSS.grad = grad; //rubbish2.col(0);
    inputsSS.p = p;
    inputsSS.p0 = p0;
    inputsSS.v = v;
    inputsSS.F = yFitV;
    inputsSS.d_t = d_t; //rubbish(0);
    inputsSS.innVariance = innVariance; //rubbish(1);
    inputsSS.objFunValue = objFunValue; //rubbish(2);
    inputsSS.cLlik = true; //rubbish(3);
    inputsSS.outlier = outlier;
//     vec aux(1); aux(0) = inputsSS.outlier;
//     if (aux.has_nan()){
//         inputsSS.outlier = 0;
//     }
    inputsSS.Iter = Iter; //rubbish(6);
    inputsSS.verbose = verbose;
    inputsSS.estimOk = estimOk;
    inputsSS.nonStationaryTerms = nonStationaryTerms;
    inputsSS.criteria = criteria;
    inputsSS.betaAug = betas;
    inputsSS.betaAugVar = betaV;

    inputsBSM.seas = seas; //rubbish(7);
    inputsBSM.stepwise = stepwise;
    //inputsBSM.ns = rubbish3.col(0);
    inputsBSM.nPar = nPar; //rubbish3.col(1);
   if (harmonics.has_nan()){
        inputsBSM.harmonics.resize(1);
        inputsBSM.harmonics(0) = 0;
    } else {
        inputsBSM.harmonics = conv_to<uvec>::from(harmonics);
    }
    inputsBSM.constPar = constPar; //rubbish2.col(1);
    inputsBSM.typePar = typePar; //rubbish2.col(2);
    inputsBSM.typeOutliers = typeOutliersp;
    inputsBSM.arma = arma; //rubbish(5);
    inputsBSM.MSOE = MSOE;
    inputsBSM.PTSnames = PTSnames;
    // BoxCox transformation
    if (lambdaBoxCox == 9999.9)
        lambdaBoxCox = testBoxCox(y, periods);
    inputsBSM.lambda = lambdaBoxCox;
    inputsSS.y = BoxCox(inputsSS.y, inputsBSM.lambda);
    // inputsBSM.iniObs = iniObs;
    // Building model
    BSMclass sysBSM = BSMclass(inputsSS, inputsBSM);
    // Commands
    SSinputs inputs;
    BSMmodel inputs2;
    // End of wrapper adaptation

   if (command == "estimate"){
         // Estimating and Forecasting
       sysBSM.estim(inputsSS.verbose);
       sysBSM.forecast();

        // Values to return
        inputs = sysBSM.SSmodel::getInputs();
        inputs2 = sysBSM.getInputs();
        vec harmonicsVec = conv_to<vec>::from(inputs2.harmonics);
        inputsBSM.harmonics = conv_to<uvec>::from(harmonics);

        // Correcting ns
        inputs2.ns(2) = inputs2.periods.n_elem * 2 - any(inputs2.periods == 2);
        //mat pars = join_horiz(inputs.p, inputs.pTransform);
        //Further corrections due to interpolation
        if (iniObs > 0){
            if (inputs.u.n_rows > up.n_rows){  // Outlier outputs
                uIni = join_vert(uIni, zeros(inputs.u.n_rows - up.n_rows, iniObs));
            }
            if (up.n_rows > 0){
                // Check outliers that add u for outliers
                up = join_horiz(uIni, inputs.u);
            }
        } else {
            up = inputs.u;
        }
        // Back to Python
//    vector<double> p, p0Return, yFor, periods, rhos, FFor, betaAug, betaAugVar, criteria,
//                   grad, constPar, typePar, ns, nPar, harmonics, cycleLimits, u, typeOutliers;
//    string model, estimOk;
//    int nonStationaryTerms, d_t, h, iter, rowc, rowu, rowtype;
//    double innVariance, objFunValue, outlier;
        m1.p = conv_to<vector<double>>::from(inputs.p);
        m1.p0 = conv_to<vector<double>>::from(inputs2.p0Return);
        m1.model = inputs2.model;
        m1.yFor = conv_to<vector<double>>::from(inputs.yFor);
        m1.periods = conv_to<vector<double>>::from(inputs2.periods);
        m1.rhos = conv_to<vector<double>>::from(inputs2.rhos);
        m1.yForV = conv_to<vector<double>>::from(inputs.FFor);
        m1.estimOk = inputs.estimOk;
        m1.harmonics = conv_to<vector<double>>::from(harmonicsVec);
        m1.cycleLimits = conv_to<vector<double>>::from(vectorise(inputs2.cycleLimits));
        m1.rowc = inputs2.cycleLimits.n_rows;
        m1.nonStationaryTerms = nonStationaryTerms;
        m1.betaAug = conv_to<vector<double>>::from(inputs.betaAug);
        m1.betaAugVar = conv_to<vector<double>>::from(inputs.betaAugVar);
        m1.u = conv_to<vector<double>>::from(vectorise(up));
        m1.rowu = up.n_rows;
        m1.typeOutliers = conv_to<vector<double>>::from(vectorise(inputs2.typeOutliers));
        m1.rowtype = inputs2.typeOutliers.n_rows;
        m1.criteria = conv_to<vector<double>>::from(inputs.criteria);
        m1.d_t = inputs.d_t + iniObs;
        m1.innVariance = inputs.innVariance;
        m1.objFunValue = inputs.objFunValue;
        m1.grad = conv_to<vector<double>>::from(inputs.grad);
        m1.constPar = conv_to<vector<double>>::from(inputs2.constPar);
        m1.typePar = conv_to<vector<double>>::from(inputs2.typePar);
        m1.ns = conv_to<vector<double>>::from(inputs2.ns);
        m1.nPar = conv_to<vector<double>>::from(inputs2.nPar);
        m1.h = inputs.h;
        m1.outlier = inputs.outlier;
        m1.iter = inputs.Iter;
        m1.lambdaBoxCox = lambdaBoxCox;
    } else if (command == "validate"){
        sysBSM.validate(false);
        // Values to return
        inputs = sysBSM.SSmodel::getInputs();
        inputs2 = sysBSM.getInputs();
        //Back to Python
        m1.v = conv_to<vector<double>>::from(inputs.v);
        m1.table = inputs.table;
        m1.coef = conv_to<vector<double>>::from(inputs.coef);
        //plhs[3] = mxCreateString(inputs2.parNames.c_str());
    }else if(command == "filter" || command == "smooth" || command == "disturb"){
        sysBSM.setSystemMatrices();
        if (command == "filter"){
            sysBSM.filter();
        } else if (command == "smooth") {
            sysBSM.smooth(false);
        } else {
            sysBSM.disturb();
        }
        // Corrections for interpolation
        inputs = sysBSM.SSmodel::getInputs();
        inputs2 = sysBSM.getInputs();
        string statesN = stateNames(inputs2);
        if (command == "disturb"){
            uvec missing = find_nonfinite(inputs.y);
            inputs.eta.cols(missing).fill(datum::nan);
            inputs2.eps(missing).fill(datum::nan);
        }
        // Nans at very beginning
        if (iniObs > 0 && command != "disturb"){
            uvec missing = find_nonfinite(inputs.y.rows(0, iniObs));
            mat P = inputs.P.cols(0, iniObs);
            sysBSM.interpolate(iniObs);
            if (command == "filter"){
                sysBSM.filter();
            } else if (command == "smooth"){
                sysBSM.smooth(false);
            }
            inputs = sysBSM.SSmodel::getInputs();
            inputs.P.cols(0, iniObs) = P;
            inputs.v(missing).fill(datum::nan);
        }

        // Values to return
        inputs = sysBSM.SSmodel::getInputs();
        inputs2 = sysBSM.getInputs();

        //Back to Python
        m1.a = conv_to<vector<double>>::from(vectorise(inputs.a));
        m1.rowa = inputs.a.n_rows;
        m1.P = conv_to<vector<double>>::from(vectorise(inputs.P));
        m1.rowP = inputs.P.n_rows;
        m1.v = conv_to<vector<double>>::from(inputs.v);
        m1.F = conv_to<vector<double>>::from(inputs.F);
        m1.yFit = conv_to<vector<double>>::from(inputs.yFit);
        if (command == "disturb"){
            m1.eps = conv_to<vector<double>>::from(inputs2.eps);
            m1.eta = conv_to<vector<double>>::from(vectorise(inputs.eta));
            m1.roweta = inputs.eta.n_rows;
        }
        m1.stateNames = statesN;

    }else if (command == "components"){
        sysBSM.setSystemMatrices();
        sysBSM.components();
        inputs2 = sysBSM.getInputs();
        string compNames = inputs2.compNames;
        // Nans at very beginning
        if (iniObs > 0){
            inputs = sysBSM.SSmodel::getInputs();
            uvec missing = find_nonfinite(inputs.y.rows(0, iniObs));
            //vec ytrun = inputs.y.rows(0, iniObs);
            mat P = inputs2.compV.cols(0, iniObs);
            sysBSM.interpolate(iniObs);
            sysBSM.components();
            inputs2 = sysBSM.getInputs();
            inputs2.compV.cols(0, iniObs) = P;
            // Setting irregular to nan
            uvec rowI(1); rowI(0) = 0;
            if (compNames.find("Level") != string::npos)
                rowI++;
            if (compNames.find("Slope") != string::npos)
                rowI++;
            if (compNames.find("Seasonal") != string::npos)
                rowI++;
            if (compNames.find("Irr") != string::npos ||
                compNames.find("ARMA") != string::npos)
                inputs2.comp.submat(rowI, missing).fill(datum::nan);
        }
        // Values to return
        inputs2 = sysBSM.getInputs();
        //Back to Python
        m1.comp = conv_to<vector<double>>::from(vectorise(inputs2.comp));
        m1.rowcomp = inputs2.comp.n_rows;
        m1.compV = conv_to<vector<double>>::from(vectorise(inputs2.compV));
        m1.compNames = compNames;
    }
   return m1;
}

PYBIND11_MODULE(UCc, m){
    py::class_<BSMreturn>(m, "BSMreturn").def_readwrite("p", &BSMreturn::p)
          .def_readwrite("p0", &BSMreturn::p0)
          .def_readwrite("yFor", &BSMreturn::yFor)
          .def_readwrite("periods", &BSMreturn::periods)
          .def_readwrite("rhos", &BSMreturn::rhos)
          .def_readwrite("yForV", &BSMreturn::yForV)
          .def_readwrite("betaAug", &BSMreturn::betaAug)
          .def_readwrite("betaAugVar", &BSMreturn::betaAugVar)
          .def_readwrite("criteria", &BSMreturn::criteria)
          .def_readwrite("grad", &BSMreturn::grad)
          .def_readwrite("constPar", &BSMreturn::constPar)
          .def_readwrite("typePar", &BSMreturn::typePar)
          .def_readwrite("ns", &BSMreturn::ns)
          .def_readwrite("nPar", &BSMreturn::nPar)
          .def_readwrite("harmonics", &BSMreturn::harmonics)
          .def_readwrite("cycleLimits", &BSMreturn::cycleLimits)
          .def_readwrite("u", &BSMreturn::u)
          .def_readwrite("typeOutliers", &BSMreturn::typeOutliers)
          .def_readwrite("coef", &BSMreturn::coef)
          .def_readwrite("a", &BSMreturn::a)
          .def_readwrite("P", &BSMreturn::P)
          .def_readwrite("v", &BSMreturn::v)
          .def_readwrite("F", &BSMreturn::F)
          .def_readwrite("yFit", &BSMreturn::yFit)
          .def_readwrite("eps", &BSMreturn::eps)
          .def_readwrite("eta", &BSMreturn::eta)
          .def_readwrite("comp", &BSMreturn::comp)
          .def_readwrite("compV", &BSMreturn::compV)
          .def_readwrite("model", &BSMreturn::model)
          .def_readwrite("estimOk", &BSMreturn::estimOk)
          .def_readwrite("stateNames", &BSMreturn::stateNames)
          .def_readwrite("compNames", &BSMreturn::compNames)
          .def_readwrite("nonStationaryTerms", &BSMreturn::nonStationaryTerms)
          .def_readwrite("d_t", &BSMreturn::d_t)
          .def_readwrite("h", &BSMreturn::h)
          .def_readwrite("iter", &BSMreturn::iter)
          .def_readwrite("rowc", &BSMreturn::rowc)
          .def_readwrite("rowu", &BSMreturn::rowu)
          .def_readwrite("rowtype", &BSMreturn::rowtype)
          .def_readwrite("rowa", &BSMreturn::rowa)
          .def_readwrite("rowP", &BSMreturn::rowP)
          .def_readwrite("roweta", &BSMreturn::roweta)
          .def_readwrite("rowcomp", &BSMreturn::rowcomp)
          .def_readwrite("innVariance", &BSMreturn::innVariance)
          .def_readwrite("objFunValue", &BSMreturn::objFunValue)
          .def_readwrite("outlier", &BSMreturn::outlier)
          .def_readwrite("lambdaBoxCox", &BSMreturn::lambdaBoxCox)
          .def_readwrite("table", &BSMreturn::table);
    m.def("UCfunC", &UCfunC);
}
