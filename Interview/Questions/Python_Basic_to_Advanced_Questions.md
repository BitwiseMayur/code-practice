1. Is Python a compiled language or an interpreted language?
   Python is a hybrid language that combines both compiled and interpreted features. Let me explain:

	Compilation Aspect:
	When you write a Python program, it is first compiled into an intermediate form called **bytecode**.
	This compilation step is hidden from the programmer, making Python appear as an interpreted language.
	The bytecode is generated when you execute your code, and it resides in files with the .pyc extension.
	
	Interpretation Aspect:
	The Python interpreter then interprets this **bytecode line by line**.
	It converts the bytecode into machine instructions that the underlying platform (machine and operating system) can 			execute.
	The compiled bytecode is not visible to the programmer during execution.

 2. What do you mean by Dynamically Typed Language?
	The type of the variable is determined at the run-time. We declare a = 10, we do not explicitly mention the type here.

 3. How are arguments passed by value or by reference in Python?
	Neither, in Python everything is an Object and the variables hold references to these Objects. These reference will be 		passed to the functions. For Immutable objects like string, integers etc Python creates a new reference to the same 		object. Any change to the object will only be reflected in the funciton scope. For Mutable objects, Python passes the 		reference to the object due to which any changes made will be reflected outside the funciton as well. 
