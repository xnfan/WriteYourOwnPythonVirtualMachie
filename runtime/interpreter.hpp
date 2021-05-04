# ifndef INTERPRETER_HPP
# define INTERPRETER_HPP

# include "code/bytecode.hpp"
# include "code/codeObject.hpp"


class Interpreter {
    private:
        HiObject * _exception_class;

    public:
        void run(CodeObject * codes);
};

# endif