import { ReactElement, useState } from "react";

export const BirdingRecord = (): ReactElement => {

    const [birds, setBirds] = useState([]);

    const species = [
        "청호반새", "호반새", "쇠찌르레기", "큰오색딱따구리", "청다리도요"
    ]

    const saveRecord = async () => {
        alert('저장되었습니다')
    }

    const kakaoMapOption = {
        level: 3
    }

    return (
        <>
            <div
                style={{ flexDirection: 'row' }}>
                관찰기록 등록하기
            </div>
            
            <button onClick={saveRecord}>저장</button>
        </>
    );
}