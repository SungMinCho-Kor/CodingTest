import Foundation

let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
let n = input.first!
let m = input.last!

print(abs(n-m))