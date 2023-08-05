import {IDisposable, DisposableDelegate} from '@lumino/disposable';

import {
    JupyterFrontEnd,
    JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {ToolbarButton, InputDialog} from '@jupyterlab/apputils';

import {DocumentRegistry} from '@jupyterlab/docregistry';

// import fetch from 'node-fetch';

import {NotebookPanel, INotebookModel} from '@jupyterlab/notebook';

const plugin: JupyterFrontEndPlugin<void> = {
    activate,
    id: 'toolbar-button',
    autoStart: true
};

type VM = {
    id: string;
    name: string;
};

type AvailableVMResponse = {
    data: VM[];
};

export class ButtonExtension
    implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel> {
    createNew(
        panel: NotebookPanel,
        context: DocumentRegistry.IContext<INotebookModel>
    ): IDisposable {
        let availableVm: AvailableVMResponse | undefined = undefined;
        const getAvailableVm = async () => {
            const available_vm_response = await fetch(
                'http://localhost:8080/available_vm',
                {
                    method: 'GET',
                    headers: {
                        Accept: 'application/json'
                    }
                }
            );
            if (!available_vm_response.ok) {
                throw new Error(`Error! status: ${available_vm_response.status}`);
            }
            availableVm = (await available_vm_response.json()) as AvailableVMResponse;
        };
        getAvailableVm().catch(e => {
            throw e;
        });
        console.log(availableVm);
        const switchVM = async () => {
            let items: string[];
            if (availableVm != undefined) {
                items = availableVm.data.map(it => it.name);
            } else {
                items = ['current vm'];
            }
            return InputDialog.getItem({
                title: 'Switch to vm',
                items: items
            }).then(async result => {
                if (result.button.accept && availableVm != undefined) {
                    let vm = availableVm.data.find(it => it.name === result.value);
                    const sleep = (ms : number) => new Promise(r => setTimeout(r, ms));
                    if (vm != undefined) {
                        await sleep(10000);
                        const response =  await fetch('http://localhost:8080/switch_vm', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(vm)
                        });
                        if (!response.ok) {
                            throw new Error('failed to switch vm');
                        }
                        if (response.body == null) {
                            window.location.href = document.location.href
                        } else {
                            window.location.href = await response.text()
                        }
                    }
                }
            })
        };

        const button = new ToolbarButton({
            className: 'Move state',
            label: 'Move state',
            onClick: switchVM,
            tooltip: 'Move state'
        });

        panel.toolbar.insertItem(10, 'moveState', button);
        return new DisposableDelegate(() => {
            button.dispose();
        });
    }
}

function activate(app: JupyterFrontEnd): void {
    app.docRegistry.addWidgetExtension('Notebook', new ButtonExtension());
}

export default plugin;