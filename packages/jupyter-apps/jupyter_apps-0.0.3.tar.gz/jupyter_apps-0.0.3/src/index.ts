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

export type IJupyterApps = {
  timer: Timer,
  TimerView: (props: ITimerViewProps) => JSX.Element,
};

export const IJupyterApps = new Token<IJupyterApps>(
  '@datalayer/jupyter-apps:plugin'
);

export const jupyterApps: IJupyterApps = {
  timer,
  TimerView,
}

/**
 * The command IDs used by the jupyter-apps-widget plugin.
 */
namespace CommandIDs {
  export const create = 'create-jupyter-apps-widget';
}

/**
 * Initialization data for the @datalayer/jupyter-apps extension.
 */
const plugin: JupyterFrontEndPlugin<IJupyterApps> = {
  id: '@datalayer/jupyter-apps:plugin',
  autoStart: true,
  requires: [ICommandPalette, IJupyterDocker],
  optional: [ISettingRegistry, ILauncher],
  provides: IJupyterApps,
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    jupyterDocker: IJupyterDocker,
    settingRegistry: ISettingRegistry | null,
    launcher: ILauncher
  ): IJupyterApps => {
    const { commands } = app;
    const command = CommandIDs.create;
    commands.addCommand(command, {
      caption: 'Show Jupyter Apps',
      label: 'Jupyter Apps',
      icon: (args: any) => reactIcon,
      execute: () => {
        const content = new DatalayerWidget(jupyterDocker);
        const widget = new MainAreaWidget<DatalayerWidget>({ content });
        widget.title.label = 'Jupyter Apps';
        widget.title.icon = reactIcon;
        app.shell.add(widget, 'main');
      }
    });
    const category = 'Jupyter Apps';
    palette.addItem({ command, category, args: { origin: 'from palette' } });
    if (launcher) {
      launcher.add({
        command,
        category: 'Datalayer',
        rank: -1,
      });
    }
    console.log('JupyterLab extension @datalayer/jupyter-apps is activated!');
    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('@datalayer/jupyter-apps settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for @datalayer/jupyter-apps.', reason);
        });
    }
    requestAPI<any>('get_example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The jupyter_apps server extension appears to be missing.\n${reason}`
        );
      });
    connect('ws://localhost:8888/jupyter_apps/echo', true);
    return jupyterApps;
  }
};

export default plugin;
