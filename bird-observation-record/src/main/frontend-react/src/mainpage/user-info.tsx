import Cookies from 'js-cookie';
import { Link } from 'react-router-dom';

export { UserInfo }

const UserInfo = () => {

    let login: boolean = false
    console.log(login && true);

    return (
        <div>
            {
                login ? 
                <div>로그인돼있다</div> :
                <Link to="/login">로그인합시다</Link>
            }
        </div>
    )
}