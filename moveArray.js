
const array = [1, 2, 3, 4, 5];
const moveArray = (array, index, offset) => {
    const item = array[index];
    const item2 = array[index + offset]
    console.log(array, item);
    array.splice(index, 1, item);
    console.log(array);
    array.splice(index + offset, 1, item2);
    return array;
};

const ans = moveArray(array, 2, 1);
console.log(ans);
