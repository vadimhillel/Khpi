class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        assert new_name[0].isupper() and new_name.isidentifier()
        cls.__name__ = new_name
        
    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"
    
ReNameAbleClass.change_class_name('Newname')
print(str(ReNameAbleClass()))