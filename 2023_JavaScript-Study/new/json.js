const rabbit = {
    name: 'torri',
    color: 'white',
    size: null,
    birth: new Date(),
    jump: () => {
        console.log(`${name} can jump`);
    },
};

const json = JSON.stringify(rabbit, (key, value) => {
    console.log(`key: ${key}, value: ${value}`)
    if (key === 'name') value = 'seokhwi';
    return value;
});

// console.log(json);

const obj = JSON.parse(json, (key, value) => {
    if (key === 'birth') value = new Date();
    return value;
});

console.log(obj.birth.getDate());

