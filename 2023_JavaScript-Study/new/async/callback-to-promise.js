class UserStorage {
    loginUser(id, password) {
        return (new Promise((resolve, reject) => {
                    setTimeout(() => {
                        if (
                            (id === 'ellie' && password === 'dream') ||
                            (id === 'coder' && password === 'academy')
                        ) resolve(id);
                        else reject(new Error(`NOT FOUND`));
                    }, 1000);            
                })
        )
    }

    getRoles(user, onSuccess, onError) {
        return (new Promise((resolve, reject) => {
            setTimeout(() => {
                if (user === 'ellie') {
                    resolve({name: 'ellie', role: 'admin'})
                } else {
                    reject(new Error('NO ACCESS'))
                }    
            }, 1000)
        })
        )
    }
}

const userStorage = new UserStorage();

userStorage
    .loginUser('coder', 'academy')
    .then((id) => userStorage.getRoles(id))
    .then((info) => console.log(info))
    .catch((error) => console.log(error))
