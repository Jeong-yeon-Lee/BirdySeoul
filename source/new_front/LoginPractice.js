import React, {useState} from 'react';

const LoginPractice=()=>{
    const [username, setUsername]=useState('');
    const [password, setPassword]=useState('');
    const onChangeUsername= e =>setUsername(e.target.value);
    const onChangePassword= e =>setPassword(e.target.value);
    const onClick =()=>{
        alert(username+'님~~ !!환영합니다!');
        setUsername('');
        setPassword('');
    };
    const onKeyPress = e =>{
        if(e.key ==='Enter'){
            onClick();
        }
    }

    return(
        <div className="box">
            <h1>로그인을 합시다</h1>
            <div className="input_box">
            <input
                type="text"
                name="username"
                placeholder="아이디를 입력하세요"
                value={username}
                onChange={onChangeUsername}
            />
             <input
                type="password"
                name="password"
                placeholder="비밀번호를 입력하세요"
                value={password}
                onChange={onChangePassword}
                onKeyPress={onKeyPress}
            />
            </div>
            <button onClick={onClick}>로그인</button>
        </div>
    );

};

export default LoginPractice;