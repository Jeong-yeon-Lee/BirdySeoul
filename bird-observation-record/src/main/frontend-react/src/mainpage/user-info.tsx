import Cookies from 'js-cookie';
import { useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { LoginContext } from './login-context';

export { UserInfo }

const UserInfo = () => {

    const loginContext = useContext(LoginContext)
    const [login, setLogin] = useState(loginContext.authenticated)
    console.log(login);
    return (
        <div>
            {
                login? 
                <div>로그인돼있다</div> :
                <Link to="/login">로그인합시다</Link>
            }
        </div>
    )
}