using System;
using System.Drawing;
using System.Drawing.Text;
using System.Windows.Forms;
using BlueStacks.hyperDroid.Common;

namespace BlueStacks.hyperDroid.Frontend
{

	public class FrontendButton : Button
	{
		public FrontendButton()
		{
			this.Font = new Font(Common.Utils.GetSystemFontName(), 14, FontStyle.Bold);
			this.Height = 30;
		}

		protected override void OnPaint(PaintEventArgs evt)
		{
			evt.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;
			base.OnPaint(evt);
		}
	}

}