import pytest
from stack.stack import Stack

class StackTest:
    def setup_method(self):
        self.st = Stack()

    def test_stack_is_empty(self):
        assert self.st.is_empty()
        assert len(self.st) == 0
        assert repr(self.st) == 'Stack()'
        assert str(self.st) == 'Stack()'
        with pytest.raises(IndexError):
            self.st.pop()
        with pytest.raises(IndexError):
            self.st.top()
    
    def test_push_one_item(self):
        self.st.push(2)
        assert not self.st.is_empty()
        assert self.st.top() == 2
        assert repr(self.st) == 'Stack()'
        assert str(self.st) == 'Stack(2)'
    
    @pytest.mark.slow
    def test_push_multiple_items_until_exception_raises(self):
        for i in range(self.st.CAPACITY):
            self.st.push(i)
        assert self.st.is_full()
        with pytest.raises(OverflowError):
            self.st.push(1)
    
    # @pytest.mark.parametrize("item,name", ["3", 3.2], ["a", "b"])
    @pytest.mark.parametrize("item", ["2", True, 3.2])
    def test_push_non_integer_item(self, item):
        with pytest.raises(TypeError):
            self.st.push(item)

    def test_push_multiple_items_and_pop_multiple_items(self):
        for i in range(100):
            if i % 2 == 0:
                self.st.push(i)
            else:
                self.st.pop()
        
        assert self.st.is_empty()
    