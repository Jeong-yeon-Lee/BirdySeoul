import axios from "axios"
import { BaseSyntheticEvent, ChangeEvent, ReactElement, useState } from "react"
import { instance } from "./login-page"

export { RegisterPage }

const RegisterPage = (): ReactElement => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        <>
            <div>이메일 : </div>
            <input type="email"
                onChange={(e: ChangeEvent<HTMLInputElement>) => {
                    setEmail(e.currentTarget.value);
                }}></input>
            <div>비밀번호 : </div>
            <input type="password"
                onChange={(e: ChangeEvent<HTMLInputElement>) => {
                    setPassword(e.currentTarget.value);
                }}></input>
            <button
                onClick={async (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
                    const register = await instance.post("register", {
                        email: email,
                        password: password
                    });
                }}
            >가입하기</button>
        </>)
}