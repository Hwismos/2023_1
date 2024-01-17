'use strict'

const fetchNumber = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(1)
    }, 1000);
})

fetchNumber
    .then((num) => {
        console.log(num);
        return num;
    })
    .then((num) => {
        num = num * 5;
        console.log(num);
        return num;
    })
    .then((num) => {
        return new Promise((resolve, reject) => {
                    setTimeout(() => {
                        if (num % 2 != 0) reject(new Error(`It's not even...`))
                        resolve(num * 10);
                    }, 1000);
                })
    })
    .catch((error) => {
        console.log(error);
    })
    .then((num) => {
        console.log(num);
    })

    
const getHen = (animal = 'hen') => {
    return (
        new Promise((resolve, reject) => {
            setTimeout(() => {
                if (animal != 'hen') 
                    reject(new Error(`It's not hen...`));
                else
                    resolve('hen')
            }, 1000);
        })
    )
}

const getEgg = (hen) => {
    return (
        new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve(`${hen} -> egg`)
            }, 1000);
        })
    )
} 

const cook = (egg) => {
    return (
        new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve(`${egg} -> scrumble`)
            }, 1000);
        })
    )
}

getHen()
    .then((hen) => getEgg(hen))
    .then((egg) => cook(egg))
    .then((meal) => console.log(meal))