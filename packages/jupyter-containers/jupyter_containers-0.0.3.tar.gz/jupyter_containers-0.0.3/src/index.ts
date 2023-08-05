import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { MainAreaWidget, ICommandPalette } from '@jupyterlab/apputils';
import { ILauncher } from '@jupyterlab/launcher';
import { reactIcon } from '@jupyterlab/ui-components';
import { IJupyterDocker } from '@datalayer/jupyter-docker';
import { Token } from '@lumino/coreutils';
import { DatalayerWidget } from './widget';
import { requestAPI } from './handler';
import { connect } from './ws';
import { timer, Timer, TimerView, ITimerViewProps } from "./store";

import '../style/index.css';

export type IJupyterContainers = {
  timer: Timer,
  TimerView: (props: ITimerViewProps) => JSX.Element,
};

export const IJupyterContainers = new Token<IJupyterContainers>(
  '@datalayer/jupyter-containers:plugin'
);

export const jupyterContainers: IJupyterContainers = {
  timer,
  TimerView,
}

/**
 * The command IDs used by the jupyter-containers-widget plugin.
 */
namespace CommandIDs {
  export const create = 'create-jupyter-containers-widget';
}

/**
 * Initialization data for the @datalayer/jupyter-containers extension.
 */
const plugin: JupyterFrontEndPlugin<IJupyterContainers> = {
  id: '@datalayer/jupyter-containers:plugin',
  autoStart: true,
  requires: [ICommandPalette, IJupyterDocker],
  optional: [ISettingRegistry, ILauncher],
  provides: IJupyterContainers,
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    jupyterDocker: IJupyterDocker,
    settingRegistry: ISettingRegistry | null,
    launcher: ILauncher
  ): IJupyterContainers => {
    const { commands } = app;
    const command = CommandIDs.create;
    commands.addCommand(command, {
      caption: 'Show Jupyter Containers',
      label: 'Jupyter Containers',
      icon: (args: any) => reactIcon,
      execute: () => {
        const content = new DatalayerWidget(jupyterDocker);
        const widget = new MainAreaWidget<DatalayerWidget>({ content });
        widget.title.label = 'Jupyter Containers';
        widget.title.icon = reactIcon;
        app.shell.add(widget, 'main');
      }
    });
    const category = 'Jupyter Containers';
    palette.addItem({ command, category, args: { origin: 'from palette' } });
    if (launcher) {
      launcher.add({
        command,
        category: 'Datalayer',
        rank: -1,
      });
    }
    console.log('JupyterLab extension @datalayer/jupyter-containers is activated!');
    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('@datalayer/jupyter-containers settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for @datalayer/jupyter-containers.', reason);
        });
    }
    requestAPI<any>('get_example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The jupyter_containers server extension appears to be missing.\n${reason}`
        );
      });
    connect('ws://localhost:8888/jupyter_containers/echo', true);
    return jupyterContainers;
  }
};

export default plugin;
