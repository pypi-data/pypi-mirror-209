/*
Compile with:
c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup -I/Library/Frameworks/Python.framework/Headers
-I"/Users/diego.pedregal/Google Drive/C++/armadillo-10.8.2/include" -llapack -lblas $(python3 -m
pybind11 --includes) pythonETS.cpp -o ETSc$(python3-config --extension-suffix)
*/
#include "ETSmodel.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
//#include <pybind11/pytypes.h>
namespace py = pybind11;

class ETSreturn{       // The class
  public:             // Access specifier
    string model, compNames;
    vector<double> p, yFor, yForV, ySimul, comp;
    vector<string> table;
    double lambda;
};

ETSreturn ETSfunC(string command, vector<double> ys, vector<double> us, int rowu, int colu,
	             string model, int s, int h, bool verbose, string criterion, bool identAll,
                 vector<double> alphaLs, vector<double> betaLs, vector<double> gammaLs, vector<double> phiLs,
                 string parConstraints, bool forIntervals, bool bootstrap,
                 int nSimul, vector<double> armas, bool armaIdent, vector<double> p0s, double lambda){
    // y:       otuput data (one time series)
    // u:       input data (excluding constant)
    // rowu:    rows of u
    // colu:    cols of u
    // model:   string with three or four letters with model for error, trend and seasonal
    // s:       seasonal period
    // h:       forecasting horizon (if inputs it is recalculated as the length differences
    //          between u and y
    // verbose: shows estimation intermediate results
    // criterion: information criterion to use in identification
    // identALL: Whether to estimate all models
    // alphaL:  limits for alpha parameter
    // betaL:   limits for beta parameter
    // gammaL:  limits for gamma parameter
    // phiL:    limits for alphipha parameter
    // parConstraints: Constraints in parameters: none, standard, admissible
    // forIntervals: forecast variance calculation
    // nSimul:  number of simulations for bootstrap forecast simulation
    // arma:    ARMA(p, q) orders
    // armaIdent: identification of ARMA models on/off
    // p0: initial parameters for search
    // lambda: Box-Cox lambda parameter (9999.9 for estimation)

   // Transforming inputs into armadillo format
   vec y = ys;
   mat u;
   if (rowu > 0){
        vec aux = us;
        u = reshape(aux, colu, rowu);
        u = u.t();
   }
   rowvec alphaL = alphaLs, betaL = betaLs, gammaL = gammaLs, phiL = phiLs;
   vec arma = armas;
   vec p0 = p0s;

    // Wrapper adaptation
    if (p0.n_elem == 1 && p0(0) == -99999){
        p0.resize(0);
    }
    // Creating class
    ETSmodel input;
    // BoxCox transformation
    if (lambda == 9999.9) {
        vec periods;
        if (s > 1)
            periods = s / regspace(1, floor(s / 2));
        else {
            periods.resize(1);
            periods(0) = 1.0;
        }
        lambda = testBoxCox(y, periods);
    }
    if (abs(lambda) > 1)
        lambda = sign(lambda);
    input.lambda = lambda;
    input.y = BoxCox(input.y, input.lambda);
    // Creating class
    ETSclass m(input);
    m = preProcess(y, u, model, s, h, verbose, criterion, identAll, alphaL, betaL, gammaL, phiL,
                   parConstraints, forIntervals, bootstrap, nSimul, arma, armaIdent, p0, lambda);
    ETSreturn m1;
    if (m.inputModel.errorExit){    // ERROR
            m1.model = "error";
            return m1;
    }
    // End of wrapper adaptation

   if (command == "estimate"){
       if (m.inputModel.error == "?" || m.inputModel.trend == "?" || m.inputModel.seasonal == "?" || m.inputModel.armaIdent)
           m.ident(verbose);
       else {
           m.estim(verbose);
       }
       m.forecast();
       // Returning output
       m1.model = m.inputModel.model;
       m1.p = conv_to<vector<double>>::from(m.inputModel.p);;
       m1.yFor = conv_to<vector<double>>::from(m.inputModel.yFor);
       m1.yForV = conv_to<vector<double>>::from(m.inputModel.yForV);
       m1.lambda = lambda;
       if (bootstrap)
            m.simulate(h, m.inputModel.xn);
            // Returning output
            m1.ySimul = conv_to<vector<double>>::from(vectorise(m.inputModel.ySimul));
    } else if (command == "validate"){
        if (m.inputModel.error == "?" || m.inputModel.trend == "?" || m.inputModel.seasonal == "?" || m.inputModel.armaIdent)
            m.ident(false);
        else {
            m.estim(false);
        }
        m.validate();
        // Return to python
        m1.compNames = m.inputModel.compNames;
        m1.comp = conv_to<vector<double>>::from(vectorise(m.inputModel.comp));
        m1.table = m.inputModel.table;
    } else if (command == "components"){
        if (m.inputModel.error == "?" || m.inputModel.trend == "?" || m.inputModel.seasonal == "?" || m.inputModel.armaIdent)
            m.ident(false);
        else {
            m.estim(false);
        }
        m.components();
        // Return to python
        m1.compNames = m.inputModel.compNames;
        m1.comp = conv_to<vector<double>>::from(vectorise(m.inputModel.comp));
    }
   return m1;
}

PYBIND11_MODULE(ETSc, m){
    py::class_<ETSreturn>(m, "ETSreturn").def_readwrite("model", &ETSreturn::model)
          .def_readwrite("compNames", &ETSreturn::compNames)
          .def_readwrite("p", &ETSreturn::p)
          .def_readwrite("yFor", &ETSreturn::yFor)
          .def_readwrite("yForV", &ETSreturn::yForV)
          .def_readwrite("comp", &ETSreturn::comp)
        .def_readwrite("ySimul", &ETSreturn::ySimul)
        .def_readwrite("lambda", &ETSreturn::lambda)
        .def_readwrite("table", &ETSreturn::table);
    m.def("ETSfunC", &ETSfunC);
}


