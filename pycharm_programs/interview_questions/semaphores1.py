"""
The
same
instance
of
FooBar
will
be
passed
to
two
different
threads.Thread
A
will
call
foo()
while thread B will call bar().Modify the given program to output "foobar" n times.

Example
1:

Input: n = 1
Output: "foobar"
Explanation: There
are
two
threads
being
fired
asynchronously.One
of
them
calls
foo(),
while the other calls bar()."foobar" is being output 1 time.
"""
class FooBar(object):
    def __init__(self, n):
        self.n = n
        from threading import Semaphore
        self.semfoo = Semaphore(1)
        self.sembar = Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.semfoo.acquire()
            printFoo()
            self.sembar.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.sembar.acquire()
            printBar()
            self.semfoo.release()