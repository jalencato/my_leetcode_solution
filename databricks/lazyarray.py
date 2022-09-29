# function LazyArray(arr) {
# let callbacks = [];
#
# return {
#   map: function(fn) {
#   callbacks.push(fn);
#   return this;
#   },
#   indexOf: function(num) {
#   let arrCopy = [...arr];
#   for (let i = 0; i < callbacks.length; i++) {
#   arrCopy = arrCopy.map(a => callbacks[i](a));
#   }
#   callbacks = [];
#   for (let i = 0; i < arrCopy.length; i++) {
#   if (arrCopy[i] === num) {
#     return i;
#   }
#   }
#   }
# }
# }
#
# const arr = LazyArray([10, 20, 30, 40, 50]);
# const test1 = arr.map(x => x * 2).indexOf(40)
# const test2 = arr.map(x => x * 2).map(x => x * 3).indexOf(240)
# console.log(test1);
# console.log(test2)

add = lambda x: x + 1
print(add(4))