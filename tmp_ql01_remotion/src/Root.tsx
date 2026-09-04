import "./index.css";
import {MyComposition} from "./Composition";
import {QLBatchCompositions} from "./ql-batch/QLBatch";
import {QL01PilotStills} from "./ql01-pilot/QL01Pilot";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <MyComposition />
      <QL01PilotStills />
      <QLBatchCompositions />
    </>
  );
};
