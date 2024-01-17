const obj1 = {name: 'seokhwi', age: 25};

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

const obj2 = new Person('yurim', 24);

console.log(obj1);
console.log(obj2);

const obj3 = Object.assign({}, obj2);
console.clear();
console.log(obj3);

for (key in obj1) {
    console.log(key)
}

for (value of [1,2,3,4]) {
    console.log(value)
} 