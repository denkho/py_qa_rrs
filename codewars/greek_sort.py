greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)



# test.expect(greek_comparator('alpha', 'beta') < 0, "result should be negative")
# test.assert_equals(greek_comparator('psi', 'psi'), 0)
# test.expect(greek_comparator('upsilon', 'rho'), "result should be positive")

print(greek_comparator('alpha', 'beta'))
print(greek_comparator('psi', 'psi'))
print(greek_comparator('upsilon', 'rho'))