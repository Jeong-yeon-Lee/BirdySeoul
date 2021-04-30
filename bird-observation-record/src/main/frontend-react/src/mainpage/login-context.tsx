import { createContext, ReactElement, useState} from "react";

export interface LoginState {
    jwt: string | undefined,
    authenticated: boolean,
    setAuth : (jwt: string, authenticated: boolean) => void
}

export const LoginContext = createContext<LoginState>({
    jwt: undefined,
    authenticated: false,
    setAuth: () => {}
})

export function AuthProvider({children} : { children: ReactElement}) {
    const [jwt, setJwt] = useState<string | undefined>(undefined);
    const [authenticated, setAuthenticated] = useState<boolean>(false)
    const value: LoginState = {
        jwt: jwt,
        authenticated: authenticated,
        setAuth: (jwt: string, authenticated: boolean) => {
            setJwt(jwt);
            setAuthenticated(authenticated);
        }
    }
    return (
        <LoginContext.Provider value={value}>{children}</LoginContext.Provider>
    )
}