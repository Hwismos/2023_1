// 1. 변수 선언

let a = 5;

{
    let a = 10;
    console.log(`블록 안의 변수 값은 ${a}`) // 10
}

console.log(`블록 밖의 변수 값은 ${a}`) // 5

// 2. 상수

const b = 10;

// 3. 심볼

let sym1 = Symbol('id');
let sym2 = Symbol('id');

console.log(sym1 == sym2)

// 4. Object

const obj = {'name': 'seokhwi', 'age': 25}

console.log(`이름은 ${obj.name}, 나이는 ${obj.age}`)

obj.name = 'yurim'

console.log(`이름은 ${obj.name}, 나이는 ${obj.age}`)
