import pandas as pd

syllabus = eval("""{
    "Polynomials": ["Quadratic
formula", "Completing the square",
"Discriminant", "Factorization",
"Factor theorem"],
    "Algebra": ["Simple simultaneous
equations in one or two variables",
"Solution of simple inequalities",
              "Binomial theorem with
positive whole exponents",
"Combinations and binomial
probabilities"],
    "Differentiation": [
        "Derivative of x^a (including
for fractional exponents)",
        "Derivative of e^(kx)",
        "Derivative of a sum of
functions",
        "Tangents and normals to
graphs",
        "Turning points",
        "Second order derivatives",
        "Maxima and minima",
        "Differentiation from first
principles"
    ],
    "Integration": ["Indefinite
integration as the reverse of
differentiation",
                   "Definite integrals
and the signed areas they represent",
                   "Integration of x^a
(where a neq -1) and sums thereof"],
    "Graphs": ["The graphs of
quadratics and cubics", "Graphics of
trigonometric functions",
              "Solving equations and
inequalities with graphs"],
    "Logarithms and powers": ["Laws of
logarithms and exponentials", "Solution
of the equation a^x = b"],
    "Transformations": ["Relations
between the graphs of y = f(ax)", "y =
af(x)", "y = f(x-a)", "y = f(x) + a"],
    "Geometry": ["Coordinate geometry
and vectors in the plane", "Equations
of straight lines and circles",
                "Basic properties of
circles", "Lengths of arcs of
circles"],
    "Trigonometry":
["Solution of simple trigonometric
equations", "Identities (tan x = sin
x/cos x, sin^2x + cos^2x = 1)",
                     "Periodicity of
sine, cosine and tangent", "Sine and
cosine rules for triangles"],
    "Sequences and series": ["Sequences
defined iteratively and by formulae",
"Arithmetic and geometric progressions
(sums)",

"Convergence condition for infinite
geometric progressions"]
}""".replace('\n', ''))
print(syllabus)
output = pd.DataFrame({})
for key in syllabus.keys():
    record = pd.DataFrame({key: [key] + syllabus[key]}).transpose()
    output = output._append(record)
output.columns = ['topic', 'subtopic1', 'subtopic2', 'subtopic3', 'subtopic4', 'subtopic5', 'subtopic6', 'subtopic7', 'subtopic8']
print(output)
output.to_csv('syllabus.csv')