class UserStorage {
    loginUser(id, password, onSuccess, onError) {
        setTimeout(() => {
            if (
                (id === 'ellie' && password === 'dream') ||
                (id === 'coder' && password === 'academy')
            ) {
                console.log('얘는 last 나오고 나오겠지')
                onSuccess(id);
                console.log('이거는 위에꺼 나오고 바로 나오고')
            } else {
                onError(new Error('not found'));
            }
        }, 2000);

        console.log('last')
    }

    getRoles(user, onSuccess, onError) {
        console.log('이거는 last 뒤에 바로 나오지 않을까?')
        setTimeout(() => {
            if (user === 'ellie') {
                console.log('결과 나오기 전에 출력!')
                onSuccess({name: 'ellie', role: 'admin'});
            } else {
                onError(new Error('no access'));
            }
        }, 1000);
    }
}

const user = new UserStorage();
user.loginUser(
    'ellie', 
    'dream', 
    (id) => {
        user.getRoles(id, 
                    (obj) => console.log(`Hello ${obj.name}, you have a ${obj.role} role`), 
                    (obj) => console.log(obj))
    }, 
    (obj) => console.log(obj))

