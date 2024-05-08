function performOperations(str, num) {
    console.log(`${num} + ${str} =`, num + parseFloat(str));
    console.log(`${num} - ${str} =`, num - parseFloat(str));
    console.log(`${num} * ${str} =`, num * parseFloat(str));
    console.log(`${num} / ${str} =`, num / parseFloat(str));
}

performOperations("3.5", 10);
