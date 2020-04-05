# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALleftMASMENOSleftMULDIVCOMA DIGIT DIV ELSE ID IF IGUAL INT LK LP MAIN MAS MENOS MUL PC PRINT RK RP SUM TEXT\n    ini : main\n        | vacio\n    \n    main : MAIN LK sentence RK\n         | MAIN LK vacio RK\n    \n    vacio :\n    \n    sentence : single_stmt\n            | if_stmt\n            | sentence single_stmt\n            | sentence if_stmt\n    \n    single_stmt : int_decl\n                | single_op\n                | sum_function PC\n                | print\n    \n      int_decl : INT ID IGUAL term PC\n    \n    term : term operator_plus_minus term_2\n         | term_2\n    \n    term_2 : term_2 operator_mul_div DIGIT\n            | term_2 operator_mul_div id\n            | term_2 operator_mul_div sum_function\n            | DIGIT\n            | id\n            | sum_function\n            | term\n\n    \n    sum_function : SUM LP ID RP\n    \n    operator_plus_minus : MAS\n                        | MENOS\n    \n    operator_mul_div : MUL\n                     | DIV\n    \n    single_op : ID IGUAL term PC\n    \n    print : PRINT LP ID RP PC\n          | PRINT LP TEXT RP PC\n    \n    if_stmt : IF LP ID RP LK sentence RK\n            | IF LP ID RP LK sentence RK ELSE LK sentence RK\n    \n   id : ID\n   '

_lr_action_items = {'MAIN': ([0, ], [4, ]), '$end': ([0, 1, 2, 3, 19, 22, ], [-5, 0, -1, -2, -3, -4, ]),
                    'LK': ([4, 40, 63, ], [5, 52, 64, ]), 'RK': (
    [5, 6, 7, 8, 9, 10, 11, 13, 20, 21, 23, 41, 58, 59, 60, 61, 62, 65, 66, ],
    [-5, 19, 22, -6, -7, -10, -11, -13, -8, -9, -12, -29, -14, -30, -31, 62, -32, 66, -33, ]), 'IF': (
    [5, 6, 8, 9, 10, 11, 13, 20, 21, 23, 41, 52, 58, 59, 60, 61, 62, 64, 65, 66, ],
    [14, 14, -6, -7, -10, -11, -13, -8, -9, -12, -29, 14, -14, -30, -31, 14, -32, 14, 14, -33, ]), 'INT': (
    [5, 6, 8, 9, 10, 11, 13, 20, 21, 23, 41, 52, 58, 59, 60, 61, 62, 64, 65, 66, ],
    [16, 16, -6, -7, -10, -11, -13, -8, -9, -12, -29, 16, -14, -30, -31, 16, -32, 16, 16, -33, ]), 'ID': (
    [5, 6, 8, 9, 10, 11, 13, 16, 20, 21, 23, 24, 25, 27, 28, 36, 41, 42, 43, 44, 45, 46, 47, 52, 58, 59, 60, 61, 62, 64,
     65, 66, ],
    [15, 15, -6, -7, -10, -11, -13, 26, -8, -9, -12, 29, 30, 37, 38, 30, -29, 30, -25, -26, 30, -27, -28, 15, -14, -30,
     -31, 15, -32, 15, 15, -33, ]), 'SUM': (
    [5, 6, 8, 9, 10, 11, 13, 20, 21, 23, 25, 36, 41, 42, 43, 44, 45, 46, 47, 52, 58, 59, 60, 61, 62, 64, 65, 66, ],
    [17, 17, -6, -7, -10, -11, -13, -8, -9, -12, 17, 17, -29, 17, -25, -26, 17, -27, -28, 17, -14, -30, -31, 17, -32,
     17, 17, -33, ]), 'PRINT': ([5, 6, 8, 9, 10, 11, 13, 20, 21, 23, 41, 52, 58, 59, 60, 61, 62, 64, 65, 66, ],
                                [18, 18, -6, -7, -10, -11, -13, -8, -9, -12, -29, 18, -14, -30, -31, 18, -32, 18, 18,
                                 -33, ]), 'PC': ([12, 30, 31, 32, 33, 34, 35, 48, 49, 50, 51, 53, 54, 55, 56, 57, ],
                                                 [23, -34, 41, -16, -20, -21, -22, 58, -24, 59, 60, -23, -15, -17, -18,
                                                  -19, ]), 'LP': ([14, 17, 18, ], [24, 27, 28, ]),
                    'IGUAL': ([15, 26, ], [25, 36, ]),
                    'DIGIT': ([25, 36, 42, 43, 44, 45, 46, 47, ], [33, 33, 33, -25, -26, 55, -27, -28, ]),
                    'TEXT': ([28, ], [39, ]), 'RP': ([29, 37, 38, 39, ], [40, 49, 50, 51, ]), 'MAS': (
    [30, 31, 32, 33, 34, 35, 48, 49, 53, 54, 55, 56, 57, ],
    [-34, 43, -16, -20, -21, -22, 43, -24, 43, -15, -17, -18, -19, ]), 'MENOS': (
    [30, 31, 32, 33, 34, 35, 48, 49, 53, 54, 55, 56, 57, ],
    [-34, 44, -16, -20, -21, -22, 44, -24, 44, -15, -17, -18, -19, ]), 'MUL': (
    [30, 31, 32, 33, 34, 35, 48, 49, 53, 54, 55, 56, 57, ],
    [-34, -23, 46, -20, -21, -22, -23, -24, -23, 46, -17, -18, -19, ]), 'DIV': (
    [30, 31, 32, 33, 34, 35, 48, 49, 53, 54, 55, 56, 57, ],
    [-34, -23, 47, -20, -21, -22, -23, -24, -23, 47, -17, -18, -19, ]), 'ELSE': ([62, ], [63, ]), }

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:  _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ini': ([0, ], [1, ]), 'main': ([0, ], [2, ]), 'vacio': ([0, 5, ], [3, 7, ]),
                  'sentence': ([5, 52, 64, ], [6, 61, 65, ]),
                  'single_stmt': ([5, 6, 52, 61, 64, 65, ], [8, 20, 8, 20, 8, 20, ]),
                  'if_stmt': ([5, 6, 52, 61, 64, 65, ], [9, 21, 9, 21, 9, 21, ]),
                  'int_decl': ([5, 6, 52, 61, 64, 65, ], [10, 10, 10, 10, 10, 10, ]),
                  'single_op': ([5, 6, 52, 61, 64, 65, ], [11, 11, 11, 11, 11, 11, ]), 'sum_function': (
    [5, 6, 25, 36, 42, 45, 52, 61, 64, 65, ], [12, 12, 35, 35, 35, 57, 12, 12, 12, 12, ]),
                  'print': ([5, 6, 52, 61, 64, 65, ], [13, 13, 13, 13, 13, 13, ]),
                  'term': ([25, 36, 42, ], [31, 48, 53, ]), 'term_2': ([25, 36, 42, ], [32, 32, 54, ]),
                  'id': ([25, 36, 42, 45, ], [34, 34, 34, 56, ]),
                  'operator_plus_minus': ([31, 48, 53, ], [42, 42, 42, ]),
                  'operator_mul_div': ([32, 54, ], [45, 45, ]), }

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto: _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> ini", "S'", 1, None, None, None),
    ('ini -> main', 'ini', 1, 'p_ini', 'Tuii.py', 116),
    ('ini -> vacio', 'ini', 1, 'p_ini', 'Tuii.py', 117),
    ('main -> MAIN LK sentence RK', 'main', 4, 'p_main', 'Tuii.py', 126),
    ('main -> MAIN LK vacio RK', 'main', 4, 'p_main', 'Tuii.py', 127),
    ('vacio -> <empty>', 'vacio', 0, 'p_vacio', 'Tuii.py', 134),
    ('sentence -> single_stmt', 'sentence', 1, 'p_sentence', 'Tuii.py', 142),
    ('sentence -> if_stmt', 'sentence', 1, 'p_sentence', 'Tuii.py', 143),
    ('sentence -> sentence single_stmt', 'sentence', 2, 'p_sentence', 'Tuii.py', 144),
    ('sentence -> sentence if_stmt', 'sentence', 2, 'p_sentence', 'Tuii.py', 145),
    ('single_stmt -> int_decl', 'single_stmt', 1, 'p_single_stmt', 'Tuii.py', 156),
    ('single_stmt -> single_op', 'single_stmt', 1, 'p_single_stmt', 'Tuii.py', 157),
    ('single_stmt -> sum_function PC', 'single_stmt', 2, 'p_single_stmt', 'Tuii.py', 158),
    ('single_stmt -> print', 'single_stmt', 1, 'p_single_stmt', 'Tuii.py', 159),
    ('int_decl -> INT ID IGUAL term PC', 'int_decl', 5, 'p_int_decl', 'Tuii.py', 167),
    ('term -> term operator_plus_minus term_2', 'term', 3, 'p_term', 'Tuii.py', 174),
    ('term -> term_2', 'term', 1, 'p_term', 'Tuii.py', 175),
    ('term_2 -> term_2 operator_mul_div DIGIT', 'term_2', 3, 'p_term_2', 'Tuii.py', 184),
    ('term_2 -> term_2 operator_mul_div id', 'term_2', 3, 'p_term_2', 'Tuii.py', 185),
    ('term_2 -> term_2 operator_mul_div sum_function', 'term_2', 3, 'p_term_2', 'Tuii.py', 186),
    ('term_2 -> DIGIT', 'term_2', 1, 'p_term_2', 'Tuii.py', 187),
    ('term_2 -> id', 'term_2', 1, 'p_term_2', 'Tuii.py', 188),
    ('term_2 -> sum_function', 'term_2', 1, 'p_term_2', 'Tuii.py', 189),
    ('term_2 -> term', 'term_2', 1, 'p_term_2', 'Tuii.py', 190),
    ('sum_function -> SUM LP ID RP', 'sum_function', 4, 'p_sum_function', 'Tuii.py', 202),
    ('operator_plus_minus -> MAS', 'operator_plus_minus', 1, 'p_operator_plus_minus', 'Tuii.py', 210),
    ('operator_plus_minus -> MENOS', 'operator_plus_minus', 1, 'p_operator_plus_minus', 'Tuii.py', 211),
    ('operator_mul_div -> MUL', 'operator_mul_div', 1, 'p_operator_mul_div', 'Tuii.py', 219),
    ('operator_mul_div -> DIV', 'operator_mul_div', 1, 'p_operator_mul_div', 'Tuii.py', 220),
    ('single_op -> ID IGUAL term PC', 'single_op', 4, 'p_single_op', 'Tuii.py', 228),
    ('print -> PRINT LP ID RP PC', 'print', 5, 'p_print', 'Tuii.py', 236),
    ('print -> PRINT LP TEXT RP PC', 'print', 5, 'p_print', 'Tuii.py', 237),
    ('if_stmt -> IF LP ID RP LK sentence RK', 'if_stmt', 7, 'p_if_stmt', 'Tuii.py', 245),
    ('if_stmt -> IF LP ID RP LK sentence RK ELSE LK sentence RK', 'if_stmt', 11, 'p_if_stmt', 'Tuii.py', 246),
    ('id -> ID', 'id', 1, 'p_id', 'Tuii.py', 257),
]