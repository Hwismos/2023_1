const arr = [];

for (let i = 0; i < 10; i++) {
    rand = Math.floor(Math.random() * 101);
    // console.log(rand);
    arr.push(rand);
}

arr.push(1);
arr.push(1);

// console.log(arr);

arr.forEach((num, index) => console.log(`(${index}, ${num})`));

// console.log(arr);
// arr.pop();

// console.log(arr);
// arr.splice(3, 0, 1, 2, 3);

// console.clear();
// console.log(arr);
// const concatedArr = arr.concat(10, 20, 30);
// console.log(concatedArr);

// console.clear();
// console.log(arr);
// console.log(arr.includes(389));
// console.log(arr.indexOf(1));
// console.log(arr.lastIndexOf(1));

// console.clear();
// const func = (a, b) => console.log(a+b);
// func(2,3);

console.clear();
console.log(arr.some((num) => num > 200));

console.clear();

