matcher_patterns = [
        ("EMAIL_PATTERN", [{'LIKE_EMAIL':True}]),
        ("PHONE_PATTERN" , [     
                                {'SHAPE': 'ddd'},
                                {'ORTH' : '-', "OP":'?'},
                                {'SHAPE': 'ddd'},
                                {'ORTH' : '-', "OP":'?'},
                                {'SHAPE': 'dddd'}
                        ]
        )
                ]
# regex_patterns = [
#         r'''''',
#                 ]