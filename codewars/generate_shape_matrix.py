# def generate_shape(n):
#     for i in range(n):
#         for j in range(n):
#             print('+', end='')
#         print()

def generate_shape(n: int) -> str:
    return '\n'.join(['+' * n] * n)

if __name__ == '__main__':
    generate_shape(5)