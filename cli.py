import click
            import pandas as pd
            from src.preflight import validate_manifest, plan_batches
            from src.simulator import simulate_import_jobs

            @click.group()
            def cli():
                pass

            @cli.command()
            @click.argument('csv_path')
            def validate(csv_path):
                df, issues = validate_manifest(csv_path)
                click.echo(f'Manifest rows: {len(df)}')
                if not issues:
                    click.echo('No preflight issues found.')
                    return
                for issue in issues:
                    click.echo(f"[{issue['severity'].upper()}] {issue['issue']}")

            @cli.command()
            @click.argument('csv_path')
            @click.option('--batch-size', default=1000, show_default=True)
            def chunk(csv_path, batch_size):
                df, _ = validate_manifest(csv_path)
                batches = plan_batches(df, batch_size)
                for batch in batches:
                    click.echo(f"{batch['batch_id'].iloc[0]} -> {len(batch)} documents")

            @cli.command(name='simulate-import')
            @click.argument('csv_path')
            @click.option('--batch-size', default=3, show_default=True)
            def simulate_import(csv_path, batch_size):
                df, issues = validate_manifest(csv_path)
                batches = plan_batches(df, batch_size)
                jobs = simulate_import_jobs(batches)
                click.echo('Preflight issues:')
                for issue in issues:
                    click.echo(f"- {issue['severity']}: {issue['issue']}")
                click.echo('
Simulated job results:')
                click.echo(jobs.to_string(index=False))

            if __name__ == '__main__':
                cli()
