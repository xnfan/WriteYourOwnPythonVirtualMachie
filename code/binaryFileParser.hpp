# ifndef BINARY_FILE_PARSER_HPP
# define BINARY_FILE_PARSER_HPP

# include "util/bufferedInputStream.hpp"
# include "util/arrayList.hpp"
# include "object/hiObject.hpp"
# include "object/hiString.hpp"
# include "object/hiInteger.hpp"
# include "code/codeObject.hpp"

class BinaryFileParser{
    private:
        BufferedInputStream * file_stream;
        ArrayList<HiString*> _string_table;

    public:
        BinaryFileParser(BufferedInputStream * stream);

        CodeObject * parse();
        CodeObject * get_code_object();
        HiString *   get_byte_codes();
        HiString *   get_no_table();
        int          get_int();
        HiString *   get_string();
        HiString *   get_name();

        HiString *   get_file_name();

        ArrayList<HiObject *> * get_consts();
        ArrayList<HiObject *> * get_names();
        ArrayList<HiObject *> * get_var_names();
        ArrayList<HiObject *> * get_free_vars();
        ArrayList<HiObject *> * get_cell_vars();
        ArrayList<HiObject *> * get_tuple();
};

# endif