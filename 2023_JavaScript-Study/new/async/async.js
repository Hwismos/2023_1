'use strict'

async function fetchUser() {
    // do something for 10 seconds...
    return 'ellie';
}

const user = fetchUser();
// user.then((value) => console.log(user));

// 2. await

function delay(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, ms);
    })
}

async function getApple() {
    await delay(1000);
    return 'apple';
}

async function getBanana() {
    await delay(1000);
    return 'banana';
}

// getApple()
//     .then((fruit) => {
//         console.log(fruit);
//         return getBanana()
//     })
//     .then((fruit) => {
//         console.log(fruit)
//     })

// getApple().then((fruit) => console.log(fruit))

// function getBanana() {
//     return delay(1000)
//                 .then(() => 'banana')
// }

// getBanana()
//     .then((fruit) => console.log(fruit))

async function pickFruits() {
    // return getApple()
    //         .then((apple) => {
    //             return getBanana()
    //                     .then((banana) => `${apple} + ${banana}` )
    //         })
    const apple = await getApple()
    const banana = await getBanana()

    return `${apple} + ${banana}`
}

// pickFruits()
//     .then((fruits) => console.log(fruits))

pickFruits().then((result) => console.log(result))

function pickAllFruits() {
    return Promise.all([getApple(), getBanana()])
            .then((fruits) => fruits.join(' + '))
}

// pickAllFruits().then((value) => console.log(value))

function pickOnlyOne() {
    return Promise.race([getApple(), getBanana()]);
}

pickOnlyOne().then((value) => console.log(value));

