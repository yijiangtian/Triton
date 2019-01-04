#pragma warning(disable:4067)

#if not (defined REG_SPEC || defined REG_SPEC_NO_CAPSTONE)
#error REG_SPEC have to be specified before including specs
#endif

#define TT_MUTABLE_REG    true
#define TT_IMMUTABLE_REG  false

// REG_SPEC(UPPER_NAME, LOWER_NAME, AARCH64_UPPER, AARCH64_LOWER, AARCH64_PARENT, MUTABLE)

// Thirty-one 64-bit general-purpose registers 
REG_SPEC(X0,  x0,  QWORD_SIZE_BIT-1, 0, X0,  TT_MUTABLE_REG) // x0
REG_SPEC(X1,  x1,  QWORD_SIZE_BIT-1, 0, X1,  TT_MUTABLE_REG) // x1
REG_SPEC(X2,  x2,  QWORD_SIZE_BIT-1, 0, X2,  TT_MUTABLE_REG) // x2
REG_SPEC(X3,  x3,  QWORD_SIZE_BIT-1, 0, X3,  TT_MUTABLE_REG) // x3
REG_SPEC(X4,  x4,  QWORD_SIZE_BIT-1, 0, X4,  TT_MUTABLE_REG) // x4
REG_SPEC(X5,  x5,  QWORD_SIZE_BIT-1, 0, X5,  TT_MUTABLE_REG) // x5
REG_SPEC(X6,  x6,  QWORD_SIZE_BIT-1, 0, X6,  TT_MUTABLE_REG) // x6
REG_SPEC(X7,  x7,  QWORD_SIZE_BIT-1, 0, X7,  TT_MUTABLE_REG) // x7
REG_SPEC(X8,  x8,  QWORD_SIZE_BIT-1, 0, X8,  TT_MUTABLE_REG) // x8
REG_SPEC(X9,  x9,  QWORD_SIZE_BIT-1, 0, X9,  TT_MUTABLE_REG) // x9
REG_SPEC(X10, x10, QWORD_SIZE_BIT-1, 0, X10, TT_MUTABLE_REG) // x10
REG_SPEC(X11, x11, QWORD_SIZE_BIT-1, 0, X11, TT_MUTABLE_REG) // x11
REG_SPEC(X12, x12, QWORD_SIZE_BIT-1, 0, X12, TT_MUTABLE_REG) // x12
REG_SPEC(X13, x13, QWORD_SIZE_BIT-1, 0, X13, TT_MUTABLE_REG) // x13
REG_SPEC(X14, x14, QWORD_SIZE_BIT-1, 0, X14, TT_MUTABLE_REG) // x14
REG_SPEC(X15, x15, QWORD_SIZE_BIT-1, 0, X15, TT_MUTABLE_REG) // x15
REG_SPEC(X16, x16, QWORD_SIZE_BIT-1, 0, X16, TT_MUTABLE_REG) // x16
REG_SPEC(X17, x17, QWORD_SIZE_BIT-1, 0, X17, TT_MUTABLE_REG) // x17
REG_SPEC(X18, x18, QWORD_SIZE_BIT-1, 0, X18, TT_MUTABLE_REG) // x18
REG_SPEC(X19, x19, QWORD_SIZE_BIT-1, 0, X19, TT_MUTABLE_REG) // x19
REG_SPEC(X20, x20, QWORD_SIZE_BIT-1, 0, X20, TT_MUTABLE_REG) // x20
REG_SPEC(X21, x21, QWORD_SIZE_BIT-1, 0, X21, TT_MUTABLE_REG) // x21
REG_SPEC(X22, x22, QWORD_SIZE_BIT-1, 0, X22, TT_MUTABLE_REG) // x22
REG_SPEC(X23, x23, QWORD_SIZE_BIT-1, 0, X23, TT_MUTABLE_REG) // x23
REG_SPEC(X24, x24, QWORD_SIZE_BIT-1, 0, X24, TT_MUTABLE_REG) // x24
REG_SPEC(X25, x25, QWORD_SIZE_BIT-1, 0, X25, TT_MUTABLE_REG) // x25
REG_SPEC(X26, x26, QWORD_SIZE_BIT-1, 0, X26, TT_MUTABLE_REG) // x26
REG_SPEC(X27, x27, QWORD_SIZE_BIT-1, 0, X27, TT_MUTABLE_REG) // x27
REG_SPEC(X28, x28, QWORD_SIZE_BIT-1, 0, X28, TT_MUTABLE_REG) // x28
REG_SPEC(X29, x29, QWORD_SIZE_BIT-1, 0, X29, TT_MUTABLE_REG) // x29
REG_SPEC(X30, x30, QWORD_SIZE_BIT-1, 0, X30, TT_MUTABLE_REG) // x30 (LR register)
REG_SPEC(W0,  w0,  DWORD_SIZE_BIT-1, 0, X0,  TT_MUTABLE_REG)  // w0
REG_SPEC(W1,  w1,  DWORD_SIZE_BIT-1, 0, X1,  TT_MUTABLE_REG)  // w1
REG_SPEC(W2,  w2,  DWORD_SIZE_BIT-1, 0, X2,  TT_MUTABLE_REG)  // w2
REG_SPEC(W3,  w3,  DWORD_SIZE_BIT-1, 0, X3,  TT_MUTABLE_REG)  // w3
REG_SPEC(W4,  w4,  DWORD_SIZE_BIT-1, 0, X4,  TT_MUTABLE_REG)  // w4
REG_SPEC(W5,  w5,  DWORD_SIZE_BIT-1, 0, X5,  TT_MUTABLE_REG)  // w5
REG_SPEC(W6,  w6,  DWORD_SIZE_BIT-1, 0, X6,  TT_MUTABLE_REG)  // w6
REG_SPEC(W7,  w7,  DWORD_SIZE_BIT-1, 0, X7,  TT_MUTABLE_REG)  // w7
REG_SPEC(W8,  w8,  DWORD_SIZE_BIT-1, 0, X8,  TT_MUTABLE_REG)  // w8
REG_SPEC(W9,  w9,  DWORD_SIZE_BIT-1, 0, X9,  TT_MUTABLE_REG)  // w9
REG_SPEC(W10, w10, DWORD_SIZE_BIT-1, 0, X10, TT_MUTABLE_REG) // w10
REG_SPEC(W11, w11, DWORD_SIZE_BIT-1, 0, X11, TT_MUTABLE_REG) // w11
REG_SPEC(W12, w12, DWORD_SIZE_BIT-1, 0, X12, TT_MUTABLE_REG) // w12
REG_SPEC(W13, w13, DWORD_SIZE_BIT-1, 0, X13, TT_MUTABLE_REG) // w13
REG_SPEC(W14, w14, DWORD_SIZE_BIT-1, 0, X14, TT_MUTABLE_REG) // w14
REG_SPEC(W15, w15, DWORD_SIZE_BIT-1, 0, X15, TT_MUTABLE_REG) // w15
REG_SPEC(W16, w16, DWORD_SIZE_BIT-1, 0, X16, TT_MUTABLE_REG) // w16
REG_SPEC(W17, w17, DWORD_SIZE_BIT-1, 0, X17, TT_MUTABLE_REG) // w17
REG_SPEC(W18, w18, DWORD_SIZE_BIT-1, 0, X18, TT_MUTABLE_REG) // w18
REG_SPEC(W19, w19, DWORD_SIZE_BIT-1, 0, X19, TT_MUTABLE_REG) // w19
REG_SPEC(W20, w20, DWORD_SIZE_BIT-1, 0, X20, TT_MUTABLE_REG) // w20
REG_SPEC(W21, w21, DWORD_SIZE_BIT-1, 0, X21, TT_MUTABLE_REG) // w21
REG_SPEC(W22, w22, DWORD_SIZE_BIT-1, 0, X22, TT_MUTABLE_REG) // w22
REG_SPEC(W23, w23, DWORD_SIZE_BIT-1, 0, X23, TT_MUTABLE_REG) // w23
REG_SPEC(W24, w24, DWORD_SIZE_BIT-1, 0, X24, TT_MUTABLE_REG) // w24
REG_SPEC(W25, w25, DWORD_SIZE_BIT-1, 0, X25, TT_MUTABLE_REG) // w25
REG_SPEC(W26, w26, DWORD_SIZE_BIT-1, 0, X26, TT_MUTABLE_REG) // w26
REG_SPEC(W27, w27, DWORD_SIZE_BIT-1, 0, X27, TT_MUTABLE_REG) // w27
REG_SPEC(W28, w28, DWORD_SIZE_BIT-1, 0, X28, TT_MUTABLE_REG) // w28
REG_SPEC(W29, w29, DWORD_SIZE_BIT-1, 0, X29, TT_MUTABLE_REG) // w29
REG_SPEC(W30, w30, DWORD_SIZE_BIT-1, 0, X30, TT_MUTABLE_REG) // w30

// Flag register
REG_SPEC_NO_CAPSTONE(SPSR, spsr, 31, 0, SPSR, TT_MUTABLE_REG) // SPSR

// Stack pointer registers
REG_SPEC(SP,  sp,  QWORD_SIZE_BIT-1, 0, SP, TT_MUTABLE_REG) // SP
REG_SPEC(WSP, wsp, DWORD_SIZE_BIT-1, 0, SP, TT_MUTABLE_REG) // WSP

// Program counter register
REG_SPEC_NO_CAPSTONE(PC, pc, QWORD_SIZE_BIT-1, 0, PC, TT_MUTABLE_REG) // PC

// Zero registers
REG_SPEC(XZR, xzr, QWORD_SIZE_BIT-1, 0, XZR, TT_IMMUTABLE_REG) // XZR
REG_SPEC(WZR, wzr, DWORD_SIZE_BIT-1, 0, XZR, TT_IMMUTABLE_REG) // WZR

// Unique flag registers
REG_SPEC_NO_CAPSTONE(C, c, 0, 0, C, TT_MUTABLE_REG) // C (Carry)
REG_SPEC_NO_CAPSTONE(N, n, 0, 0, N, TT_MUTABLE_REG) // N (Negative)
REG_SPEC_NO_CAPSTONE(V, v, 0, 0, V, TT_MUTABLE_REG) // V (Overflow)
REG_SPEC_NO_CAPSTONE(Z, z, 0, 0, Z, TT_MUTABLE_REG) // Z (Zero)

#undef REG_SPEC
#undef REG_SPEC_NO_CAPSTONE
#undef TT_IMMUTABLE_REG
#undef TT_MUTABLE_REG

#pragma warning(default:4067)