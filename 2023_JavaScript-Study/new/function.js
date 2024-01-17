'use stric'

function log(msg) {
    console.log(`I got message, "${msg}"`);
    return 0;
}

// const log_data = log("Hello JavaScript");
// console.log(log_data);

function changeName(obj) {
    if ('name' in obj) {
        obj.name = 'coder'
    } else {
        console.log(`name key is not defined`)
    }

}

// const obj = {'job': 'developer'}
// console.log(obj.name)
// changeName(obj)
// console.log(obj.name)

function defaultParam(name, age = 20) {
    console.log(`Hi ${name}, are you ${age} years old?`)
}

// defaultParam('seokhwi', 25);

// restParams('seokhwi', 'yurim', 'James'); -> 호이스팅

function restParams(...students) {
    for (const student of students) {
        console.log(`${student} 출석완료`)
    }
}

const dream = function dreamFunc(job) {
    console.log(`My dream is ${job}`);
}

// dream('developer')

const coffee = (price, shot) => {
    console.log(`${shot}샷은 ${price}원 입니다.`)
    return true;
}

const v = coffee(3, 2500);
console.log(v)