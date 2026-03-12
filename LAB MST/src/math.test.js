import {add} from "./math"



test ( "add numbers ",() => {
    expect(add(2,3)).toBe(5);
    expect(add(3,3)).toBe(5);
    expect(add(0,3)).toBe(5);
});