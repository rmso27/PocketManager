const emailRegex = new RegExp(/^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$/, "gm")
const isValidEmail = emailRegex.test("email_address@domain.com");

console.log(isValidEmail)