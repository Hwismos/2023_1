'use strict'

class UserStorage {
    async loginUser(id, password) {
        const user = await new Promise((resolve, reject) => {
                    setTimeout(() => {
                        if (
                            (id === 'ellie' && password === 'dream') ||
                            (id === 'coder' && password === 'academy')
                        ) resolve(id);
                        else reject(new Error('NOT FOUND...'));
                    }, 1000)
                    })
        return user;
    }

    async getRoles(user) {
        const role = await new Promise((resolve, reject) => {
                    setTimeout(() => {
                        if (user === 'ellie') {
                            resolve({name: 'ellie', role: 'admin'})
                        } else {
                            reject(new Error('NO ACCESS...'))
                        }    
                    }, 1000)
                    })
        return role;
    }
}

const userStorage = new UserStorage();
// userStorage.loginUser('ellie', 'dream')
//     .then((user) => userStorage.getRoles(user))
//     .then((role) => console.log(role))
const user = userStorage.loginUser('ellie', 'dream')
console.log(user)
const role = user.then((id) => userStorage.getRoles(id))
role.then((result) => console.log(result))