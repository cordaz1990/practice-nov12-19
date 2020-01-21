def __str__(self) -> str:
   """ Return a string representation of this Member.
   member = Member('Paul', 'Ajax', 'pgries@cs.trontoedu')
   member.__str__()
   'Paul\\nAjax\\npgries@cs.tronto.edu'
   """
    
    return '{}\n{}\n{}'.format(self.name, self.address, self.email)
   
    paul = Faculty('Paul','Ajax','pgries@cs.tronto.edu', '1234')
    str(paul)
    'paul\nAjax\npgries@cs.tronto.edu'
    print(paul)
    Paul
    Ajax
    pgries@cs.tronto.edu
