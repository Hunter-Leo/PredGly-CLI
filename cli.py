#!/usr/bin/env python
import os
import sys
import tempfile
import json
import click
import subprocess
import csv
import re

# Save original working directory before any changes
original_cwd = os.getcwd()

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
codes_dir = os.path.join(script_dir, 'codes')

@click.command()
@click.argument('sequence', type=str)
@click.option('--threshold', '-t', default=0.5, type=float, help='Probability threshold (0-1)')
@click.option('--out', '-o', type=str, help='Output JSON file path')
def main(sequence, threshold, out):
    """PredGly: Predict lysine glycation sites from protein sequence"""
    
    # Create temporary input file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp_input:
        tmp_input.write('>protein\n{}\n'.format(sequence))
        tmp_input_path = tmp_input.name
    
    # Create temporary output file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_output:
        tmp_output_path = tmp_output.name
    
    try:
        # Call original predict.py
        predict_script = os.path.join(codes_dir, 'predict.py')
        cmd = [sys.executable, predict_script, 
               '-input', tmp_input_path, 
               '-threshold', str(threshold), 
               '-output', tmp_output_path]
        
        # Change to codes directory and run
        process = subprocess.Popen(cmd, cwd=codes_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Change to codes directory and run
        process = subprocess.Popen(cmd, cwd=codes_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Check for errors - if original script fails, treat as no results
        if process.returncode != 0:
            results = []
        else:
            # Parse CSV results
            results = []
            try:
                with open(tmp_output_path, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Extract position and amino acid from fragment name like ">proteinK66"
                        fragment_name = row['Fragments name']
                        match = re.search(r'([A-Z])(\d+)$', fragment_name)
                        if match:
                            amino_acid = match.group(1)
                            position = int(match.group(2))
                            results.append({
                                'position': position,
                                'amino_acid': amino_acid,
                                'probability': float(row['Probability value'])
                            })
            except (IOError, KeyError):
                # No results file or empty results
                pass
        
        # Display table
        if results:
            click.echo('\nPredicted glycation sites:')
            click.echo('-' * 50)
            click.echo('{:<10} {:<12} {:<15}'.format('Position', 'Amino Acid', 'Probability'))
            click.echo('-' * 50)
            for r in results:
                click.echo('{:<10} {:<12} {:<15}'.format(r['position'], r['amino_acid'], r['probability']))
            click.echo('-' * 50)
            click.echo('Total sites found: {}'.format(len(results)))
        else:
            click.echo('No glycation sites predicted above threshold {}'.format(threshold))
            click.echo('Total sites found: 0')
        
        # Save to JSON if requested
        if out:
            if not os.path.isabs(out):
                out = os.path.join(original_cwd, out)
            
            output_data = {
                'sequence': sequence,
                'threshold': threshold,
                'total': len(results),
                'results': results
            }
            
            with open(out, 'w') as f:
                json.dump(output_data, f, indent=2)
            click.echo('\nResults saved to: {}'.format(out))
            
    finally:
        # Clean up temporary files
        try:
            os.unlink(tmp_input_path)
            os.unlink(tmp_output_path)
        except OSError:
            pass

if __name__ == "__main__":
    main()
