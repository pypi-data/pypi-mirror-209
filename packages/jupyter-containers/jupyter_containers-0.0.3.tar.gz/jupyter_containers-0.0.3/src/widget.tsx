import { IJupyterDocker } from '@datalayer/jupyter-docker';
import { ReactWidget } from '@jupyterlab/apputils';

import MockComponent from './component/MockComponent';

export class DatalayerWidget extends ReactWidget {
  private _jupyterDocker: IJupyterDocker;

  constructor(jupyterDocker: IJupyterDocker) {
    super();
    this._jupyterDocker = jupyterDocker;
    this.addClass('dla-Containers');
  }

  render(): JSX.Element {
    return <>
      <this._jupyterDocker.TimerView timer={this._jupyterDocker.timer}/>
      <MockComponent />
    </>
  }
}
