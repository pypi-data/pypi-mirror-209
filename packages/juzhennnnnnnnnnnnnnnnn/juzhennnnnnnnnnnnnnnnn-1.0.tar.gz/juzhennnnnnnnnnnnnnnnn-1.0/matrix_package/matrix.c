#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_ITERATIONS 100

void matrix_add(double* A, double* B, double* C, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            C[i * cols + j] = A[i * cols + j] + B[i * cols + j];
        }
    }
}

void matrix_multiply(double* A, double* B, double* C, int A_rows, int A_cols, int B_cols) {
    for (int i = 0; i < A_rows; i++) {
        for (int j = 0; j < B_cols; j++) {
            C[i * B_cols + j] = 0.0;
            for (int k = 0; k < A_cols; k++) {
                C[i * B_cols + j] += A[i * A_cols + k] * B[k * B_cols + j];
            }
        }
    }
}

void matrix_transpose(double* A, double* B, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            B[j * rows + i] = A[i * cols + j];
        }
    }
}



void swap_rows(double* A, int r1, int r2, int n) {
    double tmp;
    for (int i = 0; i < n; i++) {
        tmp = A[r1 * n + i];
        A[r1 * n + i] = A[r2 * n + i];
        A[r2 * n + i] = tmp;
    }
}

void matrix_inverse(double* A, double* invA, int n) {
    // Initialize invA to be the identity matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                invA[i * n + j] = 1.0;
            } else {
                invA[i * n + j] = 0.0;
            }
        }
    }

    // Gaussian-Jordan Elimination
    for (int i = 0; i < n; i++) {
        // Find the maximum element in the current column
        int max_row = i;
        for (int j = i + 1; j < n; j++) {
            if (abs(A[j * n + i]) > abs(A[max_row * n + i])) {
                max_row = j;
            }
        }

        // Swap the maximum row with the current row
        swap_rows(A, i, max_row, n);
        swap_rows(invA, i, max_row, n);

        // Make all rows below this one 0 in the current column
        for (int j = i + 1; j < n; j++) {
            double ratio = A[j * n + i] / A[i * n + i];
            for (int k = i; k < n; k++) {
                A[j * n + k] -= ratio * A[i * n + k];
                invA[j * n + k] -= ratio * invA[i * n + k];
            }
        }
    }

    // Make all rows above this one 0 in current column
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i - 1; j >= 0; j--) {
            double ratio = A[j * n + i] / A[i * n + i];
            for (int k = 0; k < n; k++) {
                A[j * n + k] -= ratio * A[i * n + k];
                invA[j * n + k] -= ratio * invA[i * n + k];
            }
        }
    }

    // Normalize diagonal
    for (int i = 0; i < n; i++) {
        double a = A[i * n + i];
        for (int j = 0; j < n; j++) {
            A[i * n + j] /= a;
            invA[i * n + j] /= a;
        }
    }
}









void rotate(double* A, int n, int p, int q) {
    double Apq = A[p * n + q];
    double App = A[p * n + p];
    double Aqq = A[q * n + q];

    double theta = 0.5 * atan2(2 * Apq, Aqq - App);
    double c = cos(theta);
    double s = sin(theta);

    A[p * n + p] = c * c * App - 2 * s * c * Apq + s * s * Aqq;
    A[q * n + q] = s * s * App + 2 * s * c * Apq + c * c * Aqq;
    A[p * n + q] = A[q * n + p] = 0.0;

    for (int i = 0; i < n; i++) {
        if (i != p && i != q) {
            double Aip = A[i * n + p];
            double Aiq = A[i * n + q];
            A[i * n + p] = A[p * n + i] = c * Aip - s * Aiq;
            A[i * n + q] = A[q * n + i] = s * Aip + c * Aiq;
        }
    }
}

void jacobi_eigenvalues(double* A, double* eigenvalues, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                rotate(A, n, i, j);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        eigenvalues[i] = A[i * n + i];
    }
}

