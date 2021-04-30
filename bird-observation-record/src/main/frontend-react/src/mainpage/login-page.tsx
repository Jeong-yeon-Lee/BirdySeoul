import axios, { AxiosInstance } from "axios";
import { url } from "node:inspector";
import { ChangeEvent, useContext, useState } from "react";
import { Link } from "react-router-dom";
import { AuthProvider, LoginContext } from "./login-context";

export { LoginPage }

export const instance: AxiosInstance = axios.create();

const LoginPage = (): React.ReactElement => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [accessToken, setToken] = useState('');
    const loginState = useContext(LoginContext)

    const authenticateUser = async () => {
        const { data } = await instance.post("/api/authenticate", {
            email: email, password: password
        });
        setToken(data.jwt);
        console.log(data);
        loginState.setAuth(data.jwt, true);
    }

    const getBirdingRecord = async () => {

        const { data } = await instance.get("/api/records", {
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        });
        console.log(data)
    }

    return (
        <AuthProvider>
            <>
                <div>
                    이메일 :
                <input
                        type="email"
                        value={email}
                        onChange={(e: ChangeEvent<HTMLInputElement>) => setEmail(e.currentTarget.value)}></input>
                </div>
                <div>
                    패스워드 :
                <input
                        type="password"
                        value={password}
                        onChange={(e: ChangeEvent<HTMLInputElement>) => setPassword(e.currentTarget.value)}></input>
                </div>
                <button onClick={authenticateUser}>로그인</button>
                <button onClick={getBirdingRecord}>테스트</button>
                <Link to="/register">
                    <button>회원가입</button>
                </Link>
            </>
        </AuthProvider>
    )
}