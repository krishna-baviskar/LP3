# Gradient Descent for f(x) = x^2 + 4x + 5; minimum is at x = -2.
def f(x): return x*x + 4*x + 5
def derivative(x): return 2*x + 4
x=float(input("Initial x: "))
learning_rate=float(input("Learning rate (e.g. 0.1): "))
iterations=int(input("Number of iterations: "))
for i in range(iterations):
    x -= learning_rate*derivative(x)
    if i % max(1,iterations//10)==0:
        print(f"Iteration {i+1}: x={x:.6f}, f(x)={f(x):.6f}")
print(f"Approximate minimum: x={x:.6f}, f(x)={f(x):.6f}")
