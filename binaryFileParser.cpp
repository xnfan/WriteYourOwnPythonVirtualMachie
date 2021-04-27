# include <stdio.h>
# include <assert.h>

# include "binaryFileParser.hpp"


CodeObject * BinaryFileParser::parse(){
    int magic_number = file_stream -> read_int();
    printf("magic number is 0x%x\n", magic_number);
    int moddate = file_stream -> read_int();
    printf("moddate is 0x%x\n", moddate);

    char object_type = file_stream->read();
    if (object_type == 'c'){
        CodeObject * result = get_code_object();
        printf("parse OK! \n");
        return result;
    }

    return NULL;

}

CodeObject * BinaryFileParser::get_code_object(){
    int argcount = file_stream -> read_int();
    int nlocals = file_stream -> read_int();
    int stacksize = file_stream -> read_int();
    int flags = file_stream -> read_int();
    printf("argcount, nlocals, stacksize, flags are 0x%x, 0x%x, 0x%x, 0x%x\n", argcount, nlocals, stacksize, flags);

    HiString * byte_codes = get_byte_codes();
    ArrayList<HiObject *> * consts = get_consts();
    ArrayList<HiObject *> * names = get_names();
    ArrayList<HiObject *> * var_names = get_var_names();
    ArrayList<HiObject *> * free_vars = get_free_vars();
    ArrayList<HiObject *> * cell_vars = get_cell_vars();
    HiString * file_name = get_file_name();
    HiString * module_name = get_name();
    int begin_line_no = file_stream -> read_int();
    HiString * lnotab = get_no_table();

    return new CodeObject(argcount, nlocals, stacksize, flags, byte_codes, consts, names, var_names, free_vars, cell_vars, file_name, module_name, begin_line_no, lnotab);
}