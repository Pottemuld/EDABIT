function countTrue (list) {
    let counter = 0;
    list.forEach(element => {
        if (element == true) {
            counter++;
        }
    });
    console.log(counter)
}

countTrue([true, false, false, true, false])
countTrue([false, false, false, false])
countTrue([])