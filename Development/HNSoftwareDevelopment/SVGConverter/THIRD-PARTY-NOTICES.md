# Third-party notices

## SharpVectors

This application uses the [SharpVectors](https://github.com/ElinamLLC/SharpVectors) NuGet
package to parse and render SVG files as WPF `Drawing` objects. SharpVectors is licensed
under the BSD 3-Clause license. See the package's own license file for full terms.

## SvgToXaml (Bernd Klaiber)

The post-processing logic in `Services/SvgConverterLogic.cs` that turns a SharpVectors
`DrawingGroup` into the compact XAML shape used here (inlining the clip geometry,
collapsing redundant nested `DrawingGroup`s, folding a `PathGeometry` into a single
`Geometry="F1 ..."` attribute, and padding each geometry with two invisible corner
points so its bounds always match the SVG's declared canvas size) is adapted from the
open-source [SvgToXaml](https://github.com/BerndK/SvgToXaml) project by Bernd Klaiber,
the same tool already in use for command-line conversions. Its license:

```
Copyright (c) 2015, Bernd Klaiber, bk@bkedv.de

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
