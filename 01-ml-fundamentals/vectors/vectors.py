
import math

def vector_magnitude(vector):
    squared_sum = sum(value ** 2 for value in vector)
    return math.sqrt(squared_sum)

def main():
    vector = [2, 5, 3]

    magnitude = vector_magnitude(vector)

    print("Vector:", vector)
    print("Dimensions:", len(vector))
    print("Magnitude:", round(magnitude, 3))


if __name__ == "__main__":
    main()
