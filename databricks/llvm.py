# ;; To run: gcc division.ll && ./a.out
#
# ; The first two statements declare a string and a function that are used for printing to stdout. You can ignore these.
# @.str = private constant [12 x i8] c"Output: %d\0A\00"
# @.zerostatement = private constant [15 x i8] c"denom is zero\0A\00"
# declare i32 @printf(i8*, ...)
#
# ; In this problem, we will be implementing a simple division algorithm in LLVM,
# ; which is an assembly-like language.
#
# ; You will need to understand the following commands:
#
# ; Memory: alloca, store, load
# ; Arithmetic: add, sub
# ; Conditionals: icmp [integer compare], br [branch]
#
# ; Language Reference: http://llvm.org/docs/LangRef.html
#
# ; https://tio.run/#llvm
#
#
# define i32 @convertopositive(i32 %number, i1 %ispositive) {
# br i1 %ispositive, label %returnpositive, label %returnnegative
#
# returnnegative:
# %positivenumber = sub i32 0, %number
# ret i32 %positivenumber
#
# returnpositive:
# ret i32 %number
# }
#
# define i32 @flipresult(i32 %result, i1 %iscurnumpositive, i1 %iscurdenompositive) {
# %sameside = icmp eq i1 %iscurnumpositive, %iscurdenompositive
#
# br i1 %sameside, label %returnpositive, label %returnnegative
#
# returnpositive:
# ret i32 %result
#
# returnnegative:
# %negativenumber = sub i32 0, %result
# ret i32 %negativenumber
# }
#
# define i32 @flipremain(i32 %result, i1 %iscurnumpositive) {
# br i1 %iscurnumpositive, label %returnpositive, label %returnnegative
#
# returnpositive:
# ret i32 %result
#
# returnnegative:
# %negativenumber = sub i32 0, %result
# ret i32 %negativenumber
# }
#
# define i32 @main() {
# start:
# ; Convenience: %str can be used for printing.
# %str = getelementptr inbounds [12 x i8], [12 x i8]* @.str, i32 0, i1 0
# %zerostatement = getelementptr inbounds [15 x i8], [15 x i8]* @.zerostatement, i32 0, i1 0
#
# ; Input: numerator & denominator, as registers.
# %num = add i32 0, 23
# %denom = add i32 0, 10
#
# ; Jump to start of your code.
# ; Note that there is no fall-through; we must jump to a label or return.
# br label %code
#
# ; You do not need to modify code above here.
# code:
# ; need to check if denom is 0
# %cond_zero = icmp eq i32 0, %denom
#
# br i1 %cond_zero, label %printzero, label %continue
#
# continue:
# ; note to check negative
# %isnumpositive = icmp slt i32 0, %num
# %isdenompositive = icmp slt i32 0, %denom
#
# ; convert all input to positive
# %numpositive = call i32 (i32, i1) @convertopositive(i32 %num, i1 %isnumpositive)
# %denompositive = call i32 (i32, i1) @convertopositive(i32 %denom, i1 %isdenompositive)
#
# ;call i32 (i8*, ...) @printf(i8* %str, i1 %isnumpositive)
# ;call i32 (i8*, ...) @printf(i8* %str, i1 %isdenompositive)
#
# ; init remain as input
# %remain = alloca i32
# store i32 %numpositive, i32* %remain
#
# ; init count as 0
# %count = alloca i32
# store i32 0, i32* %count
#
# br label %division
#
# division:
# ; check if remain is bigger than denom, if so proceed to sub otherwise reach end
# %compare = load i32, i32* %remain
# %cond = icmp uge i32 %compare, %denompositive
#
# br i1 %cond, label %process, label %print
#
# process:
# ; sub the remain with denom and increase %count
# %total = load i32, i32* %remain
# %result = sub i32 %total, %denompositive
# store i32 %result, i32* %remain
#
# %count_reg = load i32, i32* %count
# %count_update = add i32 1, %count_reg
# store i32 %count_update, i32* %count
#
# br label %division
#
# print:
# %quotient = load i32, i32* %count
# %remainder = load i32, i32* %remain
#
# %actualquotient = call i32 (i32, i1, i1) @flipresult(i32 %quotient, i1 %isnumpositive, i1 %isdenompositive)
# %actualremainder = call i32 (i32, i1) @flipremain(i32 %remainder, i1 %isnumpositive)
#
# call i32 (i8*, ...) @printf(i8* %str, i32 %actualquotient)
# call i32 (i8*, ...) @printf(i8* %str, i32 %actualremainder)
#
# br label %end
# 
# printzero:
# call i32 (i8*, ...) @printf(i8* %zerostatement)
#
# br label %end
#
# end:
# ret i32 1
# }